import Downloaders
from App import App

# currentFilePath = ""
# currentExtension = "mp3"
downloaderList = []
mp3Downloader = Downloaders.MusicMp3Downloader()
mp4Downloader = Downloaders.VideoMp4Downloader()
downloaderList.append(mp3Downloader)
downloaderList.append(mp4Downloader)

App(downloaderList=downloaderList)
