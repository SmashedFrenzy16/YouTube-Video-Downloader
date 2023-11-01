from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("YouTube Video Downloader")

title_label = Label(root, text = "✨ Youtube Video Downloader ✨")

title_label.pack()

link = StringVar()

paste_text = Label(root, text="Paste YouTube Video Link Below: ")

paste_text.place(x= 160 , y = 60)
      
link_enter = Entry(root, width = 70, textvariable = link)

link_enter = .place(x = 32, y = 90)
      
def download():
      
      url = YouTube(str(link.get()))
      
      video = url.streams.first()
      
      video.download()
      
      success_label = Label(root, text = 'Downloaded Successfully!', fg ="green")
      
      success_label.place(x= 180 , y = 210)



root.mainloop()
