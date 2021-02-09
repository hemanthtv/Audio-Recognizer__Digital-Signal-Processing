import pyaudio
import wave
import sys
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = int(sys.argv[1])

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
#print("Enter Name")
a="same"
#print("* recording")

WAVE_OUTPUT_FILENAME = a+".wav"
#print(WAVE_OUTPUT_FILENAME)
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

#print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()



from pydub import AudioSegment
from pydub.playback import play

#song = AudioSegment.from_wav(WAVE_OUTPUT_FILENAME)
#play(song)


import os
from pydub import AudioSegment
sound = AudioSegment.from_wav(WAVE_OUTPUT_FILENAME)
q=a+".mp3"
sound.export(q, format='mp3')
sound.export(os.path.join(r"D:\Dump",q), format='mp3')

os.system('python dejavu.py --recognize file D:\Dump\same.mp3')