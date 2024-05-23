import os
from tkinter import messagebox

from pytube import YouTube


class VideoMp4Downloader:
    def __init__(self):
        self.ext = "mp4"
    def download(self,url, folderPath):
        if(folderPath == ""):
            messagebox.showerror("Error","Please enter folder path")
        else:
            try:
                yt = YouTube(url)
                stream = yt.streams.filter(file_extension=self.ext,progressive=True).order_by('resolution').desc()[0]
                file = stream.download(folderPath)
                base, ext = os.path.splitext(file)
                newFile = base +"."+ self.ext
                os.rename(file, newFile)
            except Exception as e:
                messagebox.showerror("Error",str(e))

class MusicMp3Downloader:
    def __init__(self):
        self.ext = "mp3"

    def download(self, url, folderPath):
        if folderPath=="":
            messagebox.showerror("Error","Please enter folder path")
        else:
            try:
                yt = YouTube(url)
                stream = yt.streams.filter(only_audio=True).first()
                file = stream.download(folderPath)

                base, ext = os.path.splitext(file)
                newFile = base + "." + self.ext
                os.rename(file, newFile)
            except Exception as e:
                messagebox.showerror("Error",str(e))