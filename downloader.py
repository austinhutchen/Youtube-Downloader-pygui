#INSTRUCTIONS ON INSTAGRAM'
from pytube import YouTube
from tkinter import *

root =Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Austin's Youtube Downloader")
root.configure(bg="#f2eee3")

Label(root,text='Youtube Video Downloader',font="arial 20 bold",bg="#f2eee3").pack()
link=StringVar()
Label(root,text="Paste the Youtube link here:",font="arial 15 bold",bg="#f2eee3").place(x=40,y=68)
link_enter=Entry(root,width=40,textvariable=link).place(x=32,y=90)


def downloader():
 url=YouTube(str(link.get()))
 video=url.streams[1]
 video.download()
 Label(root,text='DOWNLOADED',font="arial 15",bg="#f2eee3",fg='red').place(x=185,y=210)

Button(root,text='DOWNLOAD',font='arial 15 bold',bg='pale violet red',padx=2,command=downloader,fg="blue").place(x=180,y=150)



root.mainloop()
