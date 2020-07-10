from tkinter import filedialog
from tkinter import Tk
from pytube import YouTube

# root = Tk()
# root.iconbitmap("iconBig.ico")
# root.withdraw()


userVid = None
userVidValidish = False




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

print("\t####################################\n\n\t\tYouTube video downloader\n\n\t####################################\n\nVideo title: %s\nVideo views: %s\n"%(videoLinked.title,videoLinked.views,))
userInput = input("Is this correct? Y/N:\n").lower()
if userInput == '':
    exit()
elif userInput == 'n':
    exit() 
elif userInput == 'y':
    try:
        #input_video = ffmpeg.input(videoLinked.streams.get_by_itag(137).download(fileDirectory,'video')) #1080p video
        #input_audio = ffmpeg.input(videoLinked.streams.get_by_itag(140).download(fileDirectory,'audio')) # get the audio
        videoLinked.streams.get_by_itag(22).download(fileDirectory) 
    except: 
        try:
            videoLinked.streams.get_by_itag(17).download(fileDirectory)#360p
        except:
            try:
                videoLinked.streams.get_by_itag(36).download(fileDirectory) 
            except:
                input("Error trying to download video. Application will now close") #Catch all in case neither video streams are available
                quit()
