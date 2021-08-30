from tkinter import *
import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

def Location():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name)

def Download():
   url = YouTube(str(link.get()))

   if(var1.get()):
       url.streams.filter(file_extension='mp4')
       stream = url.streams.get_by_itag(22)
       stream.download(Folder_Name)

   elif(var2.get()):
       url.streams.filter(only_audio=True)
       stream = url.streams.get_by_itag(140)
       stream.download(Folder_Name)

   elif (var3.get()):
       url.streams.filter(file_extension='mp4')
       stream = url.streams.get_by_itag(137)
       stream.download(Folder_Name)

   Label(root, text='Success', font='arial 15', fg="green").place(rely=0.85, relx=0.5, anchor=CENTER)


root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("YouTube downloader")

frame = tk.LabelFrame(root)
frame.place(height=80, width=500, x=0, rely=0.28)


link = StringVar()
Label(root, text = 'Paste Link Here:', font ='arial 10 bold').place(relx= 0.5 , y = 20, anchor=CENTER)
link_enter = Entry(root, width = 70,textvariable = link).place(relx= 0.5, y = 50, anchor=CENTER)

Label(root, text="Choose a file form: ").place(rely=0.30, relx=0)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

Checkbutton(root, text="Audio/Video", variable=var1).place(rely=0.40, relx=0.3, anchor=CENTER)
Checkbutton(root, text="Audio", variable=var2).place(rely=0.40, relx=0.50, anchor=CENTER)
Checkbutton(root, text="Video", variable=var3).place(rely=0.40, relx=0.65, anchor=CENTER)


Button(root, text='Quit', command=root.quit).place(height=25, width=40, rely=0.7, relx=0.65, anchor=CENTER)
Button(root, text='Download', command=Download).place(height=25, width=60, rely=0.7, relx=0.5, anchor=CENTER)
Button(root, text="Choose Path",command=Location).place(height=25, width=80, rely=0.7, relx=0.3, anchor=CENTER)


locationError = Label(root,text="Choose a file path")
locationError.grid(pady=165, sticky=NW)

mainloop()