from tkinter import PhotoImage

import customtkinter
import MenuCommands

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    width = 400
    height = 400


    def __init__(self,downloaderList=None):

        #main
        super().__init__()
        self.downloaderList = downloaderList
        self.geometry(f"{self.width}x{self.height}")
        self.after(201, lambda: self.iconphoto(False, PhotoImage(file="YoutubeDownloaderIcon.png")))
        self.title("Youtube Downloader")

        #menu widgets
        self.menu = Menu(self,downloaderList=self.downloaderList)


        self.mainloop()
class Menu(customtkinter.CTkFrame):
    def __init__(self, master, downloaderList=None):
        self.downloaderList = downloaderList

        super().__init__(master)
        self.create_widgets()
        self.pack(expand=True, fill="both")

    def create_widgets(self):
        input = customtkinter.CTkEntry(master=self,height=30, placeholder_text="Enter Video URL")
        input.pack(pady=10, padx=60, fill="both")

        downloadButton = customtkinter.CTkButton(master=self,text="Download", command=lambda: MenuCommands.downloadButtonPressed(url=input.get(),folderPath=MenuCommands.getFilePath(),extension=fileFormatMenu.get(), downloaderList=self.downloaderList))
        downloadButton.pack(pady=10, padx=60, fill="both")

        options = ["mp3",
                   "mp4"]

        fileFormatMenu = customtkinter.CTkOptionMenu(master=self, values=options)
        fileFormatMenu.pack(pady=10, padx=60, fill="both")

        setFolderButton = customtkinter.CTkButton(master=self, text="Set Folder",command=lambda: MenuCommands.setFilePath())
        setFolderButton.pack(pady=10, padx=60, fill="both")