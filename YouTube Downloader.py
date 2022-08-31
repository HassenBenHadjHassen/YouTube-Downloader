from pytube import YouTube
from tkinter import *
import os


#app initials
app = Tk()
app.title("YouTube Downloader")
app.geometry("350x300")


#app icon
p1 = PhotoImage(file = 'ico.png')
app.iconphoto(False, p1)

#Functions
def VideoDownload():
    try:
        # url input from user
        yt = YouTube(URL_entry.get())

        # extract Video
        video = yt.streams.get_highest_resolution()

        #destination
        destination = 'Downloaded Videos/.'

        video.download(destination)

        parseMessage = StringVar()
        parseMessage_label = Label(app, text="Download Completed!", font=("bold", 11), foreground="Green")
        parseMessage_label.grid(row=4,column=0)
    except:
        errorMessage = StringVar()
        errorMessage_label = Label(app, text="An Error \n Has occured \n please close the \n app and retry", font=("bold", 11), foreground="Red")
        errorMessage_label.grid(row=4,column=0)

def AudioDownload():
    try:
        # url input from user
        yt = YouTube(URL_entry.get())

        # extract only audio
        video = yt.streams.filter(only_audio=True).first()

        #destination
        destination = 'Downloaded Songs/.'

        # download the file
        out_file = video.download(output_path=destination)

        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        #result of success
        parseMessage = StringVar()
        parseMessage_label = Label(app, text="Download Completed!", font=("bold", 11), foreground="Green")
        parseMessage_label.grid(row=4)
    except:
        #result of error
        errorMessage = StringVar()
        errorMessage_label = Label(app, text="An Error \n Has occured \n please close the \n app and retry", font=("bold", 11), foreground="Red")
        errorMessage_label.grid(row=4)



#Vieo URL Display
URL_text = StringVar()
URL_label = Label(app, text="YouTube Link: ", font=("bold", 13), pady = 20)
URL_label.grid(row=0,column=0, sticky=W)
URL_entry = Entry(app, textvariable=URL_text)
URL_entry.grid(row=0,column=1)


#DropDown Menu
clicked = StringVar()
clicked.set("Video")
dropdown = OptionMenu(app, clicked, "Video", "Audio")
dropdown.grid(row=2, pady=20)

#function
def downlaod():
    if clicked.get() == "Video":
        VideoDownload()
    elif clicked.get() == "Audio":
        AudioDownload()

#Button
downlaod_btn = Button(app, text="Download", width=12, command=downlaod)
downlaod_btn.grid(row=3, pady=20)





#Start program
app.mainloop()







