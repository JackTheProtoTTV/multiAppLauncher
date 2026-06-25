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
areThereApps = False
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








def main():
    while True:
        appList = grabApps()
        print("-" * 26)
        print("Jack's Stream App Launcher!")
        print("-" * 26)
        print(" ")
        print("What Would You Like To Do?")
        print(" ")
        print("1. Launch Apps")
        print("2. View/Edit App List")
        print(" ")
        userChoice = input("")
        if userChoice == "1":
            if not appList:
                print("[ERROR] You need to add apps first!")
            else:
                for sublist in appList:
                    os.startfile(sublist[1])
                exit()
        elif userChoice == "2":
             while True:
                listApps()
                print(" ")
                print("What Would You Like To Do?")
                print(" ")
                print("1. Add An App")
                print("2. Remove An App")
                print(" ")
                print("(Back)")
                userChoice = input("")
                if userChoice == "1":
                     while True:
                        print("App Name? (Back)")
                        name = input("")
                        if name.lower() == "back":
                            break
                        print(" ")
                        print("App Path? (Back)")
                        path = input("")
                        if path.lower() == "back":
                            break
                        try:
                            path = Path(path)
                            if not path.is_file():
                                raise ValueError
                            addApp(name, path)
                            print("Would You Like To Add Another App?")
                            userChoice = input("")
                            if userChoice.lower() == "y":
                                continue
                            elif userChoice.lower() == "n":
                                break
                        except (ValueError, TypeError):
                            example = (r"C:\path\of\your\file.exe")
                            print(f"[ERROR] File Path must lead to executable file! ({example})")
                            continue
                elif userChoice == "2":
                     while True:
                        if not appList:
                            print("[ERROR] You need to add apps before you can remove them!")
                            break
                        else:
                            listApps()
                            print(" ")
                            print("-" * 26)
                            print("What App Would You Like To Remove?")
                            appToRemove = input("")
                            with open(appList, "r") as file:
                                if appToRemove in file.read():
                                    removeApp(appToRemove)
                                    print(" ")
                                    print("Would You Like To Remove Another App?")
                                    userChoice = input("")
                                    if userChoice.lower() == "y":
                                        continue
                                    elif userChoice.lower() == "n":
                                        break
                                    else:
                                        print("[ERROR] Please input Y or N")
                                        break
                                else:
                                    print("[ERROR] Please input valid app name!")

                elif userChoice.lower() == "back":
                     break
                else:
                     print("[ERROR] Please input 1, 2, or back!")
        else:
             print("[ERROR] Please input either 1 or 2!")
             continue
                        
                          
         

if __name__ == "__main__":
    main()
