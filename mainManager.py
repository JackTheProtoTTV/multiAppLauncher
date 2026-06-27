import subprocess
from pathlib import Path
import os
from functions import grabApps, launchApps, listApps, addApp, removeApp

areThereApps = False






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
                launchApps()
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
                            print("Would You Like To Add Another App? (Y/N)")
                            userChoice = input("")
                            if userChoice.lower() == "y":
                                continue
                            elif userChoice.lower() == "n":
                                break
                            else:
                                print("[ERROR] Please input Y or N")
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
                                    print("Would You Like To Remove Another App? (Y/N)")
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
