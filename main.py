import os
from time import  sleep

url = "https://www.youtube.com/watch?v=oAvYl_6V8rE"
"""
@define function to generate URL from YouTube Link
"""
def generate_url(url):
    import pafy
    video = pafy.new(url)
    best = video.getbestaudio()
    return best.url

def init_player():
    import vlc

    player = vlc.MediaPlayer(generate_url(url))
    player.play()
    print("Started Playing")

    sleep(10)
    while player.is_playing():
        sleep(1)
