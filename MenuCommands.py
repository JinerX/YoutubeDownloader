from tkinter.filedialog import askdirectory


def setFilePath():
    path = '{}'.format(askdirectory())
    # global currentFilePath
    # currentFilePath = path
    with open("folderPath.txt","w") as folderPath:
        folderPath.truncate(0)
        folderPath.write(path)

def getFilePath():
    try:
        with open("folderPath.txt", "r") as folderPath:
            currentFilePath = folderPath.readline()
    except FileNotFoundError:
        currentFilePath = ""
    return currentFilePath

def downloadButtonPressed(url, folderPath, extension, downloaderList):
    for d in downloaderList:
        if d.ext == extension:
            d.download(url, folderPath)
            break

