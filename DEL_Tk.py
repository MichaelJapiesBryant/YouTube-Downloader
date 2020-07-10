from tkinter import *
import tkinter as tk

#-=-=-=-=-=-=-= mainWindow setup =-=-=-=-=-=-=-=-#

root = Tk()

#Set the icon 
root.iconbitmap('icon.ico')
root.title("YouTube Downloader")
root.geometry("600x400")

#Labels
LblYouTubeLink = Label(root, text="Please enter the YouTube link      ")
LabeltypeSelect = Label(root, text="Please select what you want to download")

entryLink = tk.Entry(root, width=50)


#Label Positioning
LblYouTubeLink.grid(row=2, column=0)
LabeltypeSelect.grid(row=1, column=2)
#Entry positioning
entryLink.grid(row = 2, column = 2)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

root.mainloop()


#See the wireframes for the layout. Gonna need to make that badboy look good



#To list all the mp4 streams, TRY EXCEPT on these
#>>> yt.streams.filter(subtype='mp4')
#  [<Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2">,
#   <Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2">,
#   <Stream: itag="137" mime_type="video/mp4" res="1080p" fps="30fps" vcodec="avc1.640028">,
#   <Stream: itag="136" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.4d401f">,
#   <Stream: itag="135" mime_type="video/mp4" res="480p" fps="30fps" vcodec="avc1.4d401e">,
#   <Stream: itag="134" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.4d401e">,
#   <Stream: itag="133" mime_type="video/mp4" res="240p" fps="30fps" vcodec="avc1.4d4015">,
#   <Stream: itag="160" mime_type="video/mp4" res="144p" fps="30fps" vcodec="avc1.4d400c">,
#   <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2">]


# #For Only the Audio streams
# >>> yt.streams.filter(only_audio=True)
#   [<Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2">,
#   <Stream: itag="171" mime_type="audio/webm" abr="128kbps" acodec="vorbis">,
#   <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus">,
#   <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus">,
#   <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus">]