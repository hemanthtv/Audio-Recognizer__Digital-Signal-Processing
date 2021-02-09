import eyed3
import os

#a="[iSongs.info] 01 - Mamathala Thalli"+".mp3"
audiofile = eyed3.load(os.path.join(r"C:\Users\Hemanth\dejavu\mp3","Samajavaragamana-Naasongs.me.mp3"))
audiofile.tag.title="https://www.youtube.com/watch?v=OCg6BWlAXSw"
audiofile.tag.save()