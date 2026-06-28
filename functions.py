import subprocess
from pathlib import Path
import os
import time

parentDirectory = Path(__file__).parent
appListFile = parentDirectory / "applist.txt"


def grabApps():
    with open(appListFile, "r", encoding="utf-8") as file:
                rawAppList = file.readlines() #OBS, Path
                apps = [item.rstrip('\n') for item in rawAppList] # ['Obs,Path', 'Vnyan,path']
                fullAppList = [item.split(",") for item in apps]
                return(fullAppList)

def addApp(name, path):
      with open(appListFile, "a") as file:
            file.write(f"{name.replace('"', "")},{path}\n")

def removeApp(appName):
    with open(appListFile, "r") as file:
        allLines = file.readlines()

    safeLines = [line for line in allLines if appName not in line]

    with open(appListFile, "w") as file:
         file.writelines(safeLines)

def listApps():
    global areThereApps
    listNumber = 1
    appList = grabApps()
    if not appList:
        print("-" * 26)
        print("No Current Apps!")
        print("-" * 26)
        print(" ")
        areThereApps = False
    else:
        print("-" * 26)
        print("Current Apps")
        print("-" * 26)
        print(" ")
        areThereApps = True
    for sublist in appList:
        print(f"{listNumber}. {sublist[0]} ({sublist[1]})")
        listNumber = listNumber + 1
    print(" ")
def launchApps():
    appList = grabApps()
    for sublist in appList:
        os.startfile(sublist[1])
    exit()

def editApp(appToEdit, pathOrName, new):
    appList = grabApps()
    for sublist in appList:
        if appToEdit == sublist[0]:
            if pathOrName == "path":
                sublist[1] = new
            elif pathOrName == "name":
                sublist[0] = new
    with open (appListFile, "w") as file:
        for sublist in appList:
            file.write(f"{sublist[0]},{sublist[1]}\n")
