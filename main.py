userVid = None
userVidValidish = False
import ffmpeg
from tkinter import filedialog
from tkinter import Tk

root = Tk()
root.withdraw()

import time
import sys

toolbar_width = 40

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['



from pytube import YouTube
while (userVidValidish == False):
    userVid = input("Please enter the URL for the YouTube video you wish to download: ")

    if 'youtu' not in userVid :
        print("Please enter a valid URL")  
    elif userVid == '':
        print("Please enter a valid URL")
        continue
    else:
        print("Select the destination folder: ")
        fileDirectory = filedialog.askdirectory()
        userVidValidish = True

        
videoLinked = YouTube(userVid)

print("\t####################################\n\n\t\tMIKEYS VIDEO DOWNLOADER\n\n\t####################################\n\nVideo title: %s\nVideo views: %s\n"%(videoLinked.title,videoLinked.views))
userInput = input("Is this correct? Y/N:\n").lower()
if userInput == '':
    exit()
elif userInput == 'n':
    exit() 
elif userInput == 'y':
    try:
        input_video = ffmpeg.input(videoLinked.streams.get_by_itag(137).download(fileDirectory,'video')) #1080p video
        input_audio = ffmpeg.input(videoLinked.streams.get_by_itag(140).download(fileDirectory,'audio')) # get the audio
        #Fails at below code
        # ffmpeg.concat(input_video, input_audio, v=1, a=1).output('C:\Users\User\Desktop\Testing downloads\test\Finished.mp4').run()
    except: 
        try:
            videoLinked.streams.get_by_itag(18).download(fileDirectory) #360
        except:
            try:
                videoLinked.streams.get_by_itag(36).download(fileDirectory)
            except:
                try:
                    videoLinked.streams.get_by_itag(17).download(fileDirectory)
                except:
                    input("Error trying to download video. Application will now close")
                    quit()


# if __name__ == "__main__":
#     main()