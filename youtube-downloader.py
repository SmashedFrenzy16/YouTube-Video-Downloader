from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("YouTube Video Downloader")

Label(root, text = "✨ Youtube Video Downloader ✨".pack()

link = StringVar()

Label(root, text="Paste YouTube Video Link Below: ").place(x= 160 , y = 60)
      
link_enter = Entry(root, width = 70, textvariable = link).place(x = 32, y = 90)
      
def download():
      
      url = YouTube(str(link.get()))
      
      video = url.streams.first()
      
      video.download()
      
      Label(root, text = 'Downloaded Successfully!', fg ="green").place(x= 180 , y = 210)  



root.mainloop()
