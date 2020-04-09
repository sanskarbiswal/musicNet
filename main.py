import os
import eel
from time import  sleep

url = "https://www.youtube.com/watch?v=oAvYl_6V8rE"

"""
Initialize EEL App
"""
eel.init('web')
"""
@define function to generate URL from YouTube Link
"""
@eel.expose
def generate_url(url):
    #print("Generating URL")
    import pafy
    music = pafy.new(url)
    best = music.getbestaudio()
    metaData = {
        'title' : music.title,
        'author': music.author,
        'thumb' : music.thumb
    }
    url = best.url
    eel.music_url(url, metaData)

# @brief Handle Operations in System File
@eel.expose
def on_SysStart():
    # Check and Manage File System
    if not os.path.exists('user/'):
        print("Creating User Directory")
        #os.mkdir('user')
# @define testing flow of code
@eel.expose
def test():
    print("Testing")

# @define function to smoothly exit when main window is closed
@eel.expose
def handle_exit(ar1,ar2):
    import sys
    sys.exit(0)


if __name__ == "__main__":
    #os.system('cls')
    size = (1000,700)
    app_opt = {
        'mode' : "chrome",
        'close_callback' : handle_exit
    }
    eel.start('main.html', options=app_opt, size=size, suppress_error=True)
    
