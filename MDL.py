# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:59:43 2022

@author: Spectre71
"""

#Importing necessary libraries

from pytube import YouTube
#from cx_Freeze import setup, Executable #?
#import moviepy.editor as mp
import os
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import filedialog as fd
import sys
import urllib.request as ur
import requests as r
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import VideoClip

#Part 1: Incarnation (creating the GUI)
vkno=Tk()
con=Text(vkno,width=90,height=10)
con.place(x=30,y=200)
vkno.title("MVDL")
vkno.geometry("800x400")
vkno.resizable(0,0)

url=tk.StringVar()
aurl=tk.StringVar()
name=tk.StringVar()

def write(*message, end = "\n", sep = " "):
    text = ""
    for item in message:
        text += "{}".format(item)
        text += sep
    text += end
    con.insert(INSERT, text)

def VIMEO():

    AURL=aurl.get()
    NAME=name.get()
    write("url: "+AURL)
    write("name: "+NAME)

    PTH()

    target=AURL
    if target[-1]=="/":
        target=target[:-1]
    vID=target.split("/")[-1]
    write(vID)

    vconfigu="https://player.vimeo.com/video/"+vID+"/config"
    vconf_resp=r.get(vconfigu)
    vconf_json=vconf_resp.json()
    write(vconf_json)

    vconfig=vconf_json["request"]["files"]["progressive"][0]
    vu=vconfig["url"]
    vname="name.mp4"
    vresp=r.get(vu)
    vfile=open(vname,"wb")
    vfile.write(vresp.content)
    vfile.close()
    os.rename("name.mp4",NAME+".mp4")
    aurl.set("")
    name.set("")
    write("There ya go!")
    

def PTH():
    p=tk.filedialog.askdirectory()
    os.chdir(p)

def ofp():

    URL=url.get()
    NAME=name.get()
    write("url: "+URL)
    write("name: "+NAME)
    write("Now relax, sit back and wait for the DL to finish ;)\n")
    url.set("")
    name.set("")
    
    PTH()
    
    video = YouTube(URL)
    V_strm=video.streams.get_by_itag(17)
    write(V_strm)
    write(V_strm.title)
    V_strm.download(filename="name.mp4")
    
    os.rename("name.mp4",NAME+".mp4")

def tfp():
    
    URL=url.get()
    NAME=name.get()
    write("url: "+URL)
    write("name: "+NAME)
    write("Now relax, sit back and wait for the DL to finish ;)\n")
    url.set("")
    name.set("")

    PTH()
    
    video = YouTube(URL)
    V_strm=video.streams.get_by_itag(242)
    write(V_strm)
    write(V_strm.title)
    V_strm.download(filename="name.mp4")
    
    os.rename("name.mp4",NAME+".mp4")

def tsp():
    
    URL=url.get()
    NAME=name.get()
    write("url: "+URL)
    write("name: "+NAME)
    write("Now relax, sit back and wait for the DL to finish ;)\n")
    url.set("")
    name.set("")

    PTH()
    
    video = YouTube(URL)
    V_strm=video.streams.get_by_itag(18)
    write(V_strm)
    write(V_strm.title)
    V_strm.download(filename="name.mp4")
   
    os.rename("name.mp4",NAME+".mp4")

def fep():
    
    URL=url.get()
    NAME=name.get()
    write("url: "+URL)
    write("name: "+NAME)
    write("Now relax, sit back and wait for the DL to finish ;)\n")
    url.set("")
    name.set("")

    PTH()
    
    video = YouTube(URL)
    V_strm=video.streams.get_by_itag(244)
    write(V_strm)
    write(V_strm.title)
    V_strm.download(filename="name.mp4")
    
    os.rename("name.mp4",NAME+".mp4")

def stp():
    
    URL=url.get()
    NAME=name.get()
    write("url: "+URL)
    write("name: "+NAME)
    write("Now relax, sit back and wait for the DL to finish ;)\n")
    url.set("")
    name.set("")

    PTH()
    
    video = YouTube(URL)
    V_strm=video.streams.get_by_itag(22)
    write(V_strm)
    write(V_strm.title)
    V_strm.download(filename="name.mp4")
    
    os.rename("name.mp4",NAME+".mp4")

def tep():
    
    URL=url.get()
    NAME=name.get()
    write("url: "+URL)
    write("name: "+NAME)
    write("Now relax, sit back and wait for the DL to finish ;)\n")
    url.set("")
    name.set("")

    PTH()
    
    video = YouTube(URL)
    V_strm=video.streams.get_by_itag(248)
    write(V_strm)
    write(V_strm.title)
    V_strm.download(filename="name.mp4")
    
    os.rename("name.mp4",NAME+".mp4")

def ffp():
    
    URL=url.get()
    NAME=name.get()
    write("url: "+URL)
    write("name: "+NAME)
    write("Now relax, sit back and wait for the DL to finish ;)\n")
    url.set("")
    name.set("")

    PTH()
    
    video = YouTube(URL)
    V_strm=video.streams.get_by_itag(271)
    write(V_strm)
    write(V_strm.title)
    V_strm.download(filename="name.mp4")
   
    os.rename("name.mp4",NAME+".mp4")

def tosp():
    
    URL=url.get()
    NAME=name.get()
    write("url: "+URL)
    write("name: "+NAME)
    write("Now relax, sit back and wait for the DL to finish ;)\n")
    url.set("")
    name.set("")

    PTH()
    
    video = YouTube(URL)
    V_strm=video.streams.get_by_itag(313)
    write(V_strm)
    write(V_strm.title)
    V_strm.download(filename="name.mp4")
   
    os.rename("name.mp4",NAME+".mp4")

def fttp():
    
    URL=url.get()
    NAME=name.get()
    write("url: "+URL)
    write("name: "+NAME)
    write("Now relax, sit back and wait for the DL to finish ;)\n")
   
    PTH()

    video = YouTube(URL)
    V_strm=video.streams.get_by_itag(571)
    write(V_strm)
    write(V_strm.title)
    V_strm.download(filename="name.mp4")

    os.rename("name.mp4",NAME+".mp4")
    

def MDL():
    
    URL=url.get()
    NAME=name.get()
    write("url: "+URL)
    write("name: "+NAME)
    write("Now relax, sit back and wait for the DL to finish ;)\n")
    url.set("")
    name.set("")

    PTH()
    
    video = YouTube(URL)
    M=video.streams.filter(only_audio=True).all()
    
    M[0].download(filename="name.mp3")
   
    os.rename("name.mp3",NAME+".mp3")
    

def Exit():
    
   # write("Ajde!")
    sys.exit()
    
NLabel1=tk.Label(vkno,text="YT url: ")
reci1=tk.Entry(vkno,width=100,textvariable=url)

NLabel2=tk.Label(vkno,text="name: ")
reci2=tk.Entry(vkno,width=100,textvariable=name)

AUrl=tk.Label(vkno,text="Vimeo url: ")
AUrl.grid(row=3,column=0)
AURl=tk.Entry(vkno,width=109,textvariable=aurl)
AURl.place(x=10,y=90)
aURL=tk.Button(vkno,text="GET over here!",command=VIMEO)
aURL.place(x=9,y=115)

NLabel3=tk.Label(vkno,text="resolution:")
rez1=tk.Button(vkno,text="144p",command=ofp)
rez2=tk.Button(vkno,text="QVGA;240p",command=tfp)
rez3=tk.Button(vkno,text="EGA;360p",command=tsp)
rez4=tk.Button(vkno,text="VGA;480p",command=fep)
rez5=tk.Button(vkno,text="HD;720p",command=stp)
rez6=tk.Button(vkno,text="FHD;1080p",command=tep)
rez7=tk.Button(vkno,text="QHD;2K;1440p",command=ffp)
rez8=tk.Button(vkno,text="UHD;4K;2160p",command=tosp)
rez9=tk.Button(vkno,text="8K;4320p",command=fttp)

vno_s=tk.Button(vkno,width=50,text="Gimme da Music!",command=MDL)
ex=tk.Button(vkno,width=50,text="Exit",command=Exit)

NLabel1.grid(row=0,column=0)
reci1.grid(row=0,column=1)

NLabel2.grid(row=1,column=0)
reci2.grid(row=1,column=1)

NLabel3.grid(row=2,column=0)
rez1.place(x=75,y=45)
rez2.place(x=110,y=45)
rez3.place(x=180,y=45)
rez4.place(x=240,y=45)
rez5.place(x=301,y=45)
rez6.place(x=356,y=45)
rez7.place(x=423,y=45)
rez8.place(x=509,y=45)
rez9.place(x=594,y=45)

vno_s.place(x=40,y=150)
ex.place(x=420,y=150)

"""------------------------------------
- Add option to choose bitrate options (OPTIONAL)
- Add ability to download from any source (currently Vimeo and Youtube)
- Add proportionally scalable/movable buttons (OPTIONAL)
- Pack in .exe file
---------------------------------------"""
vkno.mainloop()

#Part 2: Video download

""" url = "link" 
video = YouTube(url)
V_strm=video.streams.get_by_itag(22)
write(V_strm)
write(V_strm.title)
V_strm.download(filename="name")

clip = mp.VideoFileClip(r"name.mp4")
clip.audio.write_audiofile(r"name.mp3")
clip.close()

os.remove("name.mp4")
"""
