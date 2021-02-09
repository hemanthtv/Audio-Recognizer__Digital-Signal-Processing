#!/usr/bin/python

import os
import sys
import json
import warnings
import argparse
import eyed3

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer
from dejavu.recognize import MicrophoneRecognizer
from argparse import RawTextHelpFormatter

warnings.filterwarnings("ignore")

DEFAULT_CONFIG_FILE = "dejavu.cnf"


def init(configpath):
    """ 
    Load config from a JSON file
    """
    try:
        with open(configpath) as f:
            config = json.load(f)
    except IOError as err:
        print("Cannot open configuration: %s. Exiting" % (str(err)))
        sys.exit(1)

    # create a Dejavu instance
    return Dejavu(config)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Dejavu: Audio Fingerprinting library",
        formatter_class=RawTextHelpFormatter)
    parser.add_argument('-c', '--config', nargs='?',
                        help='Path to configuration file\n'
                             'Usages: \n'
                             '--config /path/to/config-file\n')
    parser.add_argument('-f', '--fingerprint', nargs='*',
                        help='Fingerprint files in a directory\n'
                             'Usages: \n'
                             '--fingerprint /path/to/directory extension\n'
                             '--fingerprint /path/to/directory')
    parser.add_argument('-r', '--recognize', nargs=2,
                        help='Recognize what is '
                             'playing through the microphone\n'
                             'Usage: \n'
                             '--recognize mic number_of_seconds \n'
                             '--recognize file path/to/file \n')
    args = parser.parse_args()

    if not args.fingerprint and not args.recognize:
        parser.print_help()
        sys.exit(0)

    config_file = args.config
    if config_file is None:
        config_file = DEFAULT_CONFIG_FILE
        # print "Using default config file: %s" % (config_file)

    djv = init(config_file)
    if args.fingerprint:
        # Fingerprint all files in a directory
        if len(args.fingerprint) == 2:
            directory = args.fingerprint[0]
            extension = args.fingerprint[1]
            print("Fingerprinting all .%s files in the %s directory"
                  % (extension, directory))
            djv.fingerprint_directory(directory, ["." + extension], 4)

        elif len(args.fingerprint) == 1:
            filepath = args.fingerprint[0]
            if os.path.isdir(filepath):
                print("Please specify an extension if you'd like to fingerprint a directory!")
                sys.exit(1)
            djv.fingerprint_file(filepath)

    elif args.recognize:
        # Recognize audio source
        song = None
        source = args.recognize[0]
        opt_arg = args.recognize[1]

        if source in ('mic', 'microphone'):
            song = djv.recognize(MicrophoneRecognizer, seconds=opt_arg)
        elif source == 'file':
            song = djv.recognize(FileRecognizer, opt_arg)
        #print(song)
        print(song["song_name"])
        path=song["song_name"]+".mp3"
        audiofile = eyed3.load(os.path.join(r"C:\Users\Hemanth\dejavu\mp3",path))
        print(audiofile.tag.artist)
        print(audiofile.tag.album)
        print(audiofile.tag.title)
        
        #os.system('python download.py audiofile.tag.title')
        import pafy
        import vlc
        import sys

        url = audiofile.tag.title
        video = pafy.new(url)
        best = video.getbest()
        playurl = best.url

        Instance = vlc.Instance() #This did the trick
        player = Instance.media_player_new()
        Media = Instance.media_new(playurl)
        Media.get_mrl()

        player.set_media(Media)
        player.play()

        input()


    sys.exit(0)
