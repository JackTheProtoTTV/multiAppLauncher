import subprocess
from pathlib import Path
import os

parentDirectory = Path(__file__).parent
appList = parentDirectory / "applist.txt"


def grabApps():
    with open(appList, "r", encoding="utf-8") as file:
                rawAppList = file.readlines() #OBS, Path
                apps = [item.rstrip('\n') for item in rawAppList] # ['Obs,Path', 'Vnyan,path']
                fullAppList = [item.split(",") for item in apps]
                return(fullAppList)

def addApp(name, path):
      with open(appList, "a") as file:
            file.write(f"{name},{path}\n")

def removeApp(appName):
    with open(appList, "r") as file:
        allLines = file.readlines()

    safeLines = [line for line in allLines if appName not in line]

    with open(appList, "w") as file:
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

def launchApps():
    appList = grabApps()
    for sublist in appList:
        os.startfile(sublist[1])
        exit()