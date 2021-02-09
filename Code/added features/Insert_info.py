#!/usr/bin/env python
# coding: utf-8

# In[47]:


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
a=sys.argv[2]
print("* recording")

WAVE_OUTPUT_FILENAME = a+".wav"
print(WAVE_OUTPUT_FILENAME)
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

print("completed")
# In[48]:


from pydub import AudioSegment
from pydub.playback import play

#song = AudioSegment.from_wav(WAVE_OUTPUT_FILENAME)
#play(song)
print("completed1")

# In[49]:


import os
from pydub import AudioSegment
sound = AudioSegment.from_wav(WAVE_OUTPUT_FILENAME)
q=a+".mp3"
sound.export(os.path.join(r"C:\Users\Hemanth\dejavu\mp3",q), format='mp3')
print("completed3")

# In[50]:


import eyed3


# In[52]:


audiofile = eyed3.load(os.path.join(r"C:\Users\Hemanth\dejavu\mp3",q))

print("completed4")
# In[57]:


audiofile.tag.artist = sys.argv[2]
audiofile.tag.album = sys.argv[3]
audiofile.tag.title = sys.argv[4]
audiofile.tag.save()
print("completed5")

#os.system('python fing.py')

