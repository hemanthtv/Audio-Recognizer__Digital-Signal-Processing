'''# importing vlc module 
import vlc 
  
# importing pafy module 
import pafy 
  
# url of the video 
url = "https://www.youtube.com/watch?v=ufiWBv9h8dU"
  
# creating pafy object of the video 
video = pafy.new(url) 
  
# getting best stream 
best = video.getbest()
  
# creating vlc media player object 
media = vlc.MediaPlayer(best.url) 
  
# start playing video 
media.play() 
'''

import pafy
import vlc
import sys

url = "sys.argv[1]"
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