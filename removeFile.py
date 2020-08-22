import os

def removeExtensionFile(filePath, fileExtention) :
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            if file.name.endswith(fileExtention):
                os.remove(file.path)
        return 'Remove FIle : ' + fileExtention
    else :
        return "Directory Not Fonud"

path = input("Enter File Path : ")
file = input("Enter File Extension : ")
removeExtensionFile(path,file)