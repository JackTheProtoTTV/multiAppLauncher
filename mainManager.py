import subprocess
from pathlib import Path
import os
from functions import grabApps, launchApps, listApps, addApp, removeApp, editApp
import time
areThereApps = False
parentDirectory = Path(__file__).parent





def main():
    while True:
        appList = grabApps()
        appListFile = parentDirectory / "applist.txt"
        os.system('cls' if os.name == 'nt' else 'clear')
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
                time.sleep(1)
            else:
                launchApps()
        elif userChoice == "2":
             while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                listApps()
                print(" ")
                print("What Would You Like To Do?")
                print(" ")
                print("1. Add An App")
                print("2. Remove An App")
                print("3. Edit App")
                print(" ")
                print("(Back)")
                print(" ")
                userChoice = input("")
                if userChoice == "1":
                     while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("App Name? (Back)")
                        print(" ")
                        appList = grabApps()
                        name = input("")
                        if name.lower() == "back":
                            break
                        print(" ")
                        print("App Path? (Back)")
                        print(" ")
                        path = input("")
                        if path.lower() == "back":
                            break
                        try:
                            path = Path(path.replace('"', ""))
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
                            os.system('cls' if os.name == 'nt' else 'clear')
                            listApps()
                            appList = grabApps()
                            print(" ")
                            print("-" * 26)
                            print("What App Would You Like To Remove?")
                            print(" ")
                            print("(Back)")
                            print(" ")
                            appToRemove = input("")
                            if appToRemove.lower() == "back":
                                break
                            with open(appListFile, "r") as file:
                                if any(appToRemove in sublist[0] for sublist in appList):
                                    removeApp(appToRemove)
                                    print(" ")
                                    print("Would You Like To Remove Another App? (Y/N)")
                                    print(" ")
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
                                    time.sleep(1)
                                    continue
                elif userChoice == "3":
                    while True:
                        if not appList:
                            print("[ERROR] You need to add apps before you can edit them!")
                            break
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            listApps()
                            print("-" * 26)
                            print("What App Would You Like To Edit?")
                            print("(Back)")
                            print(" ")
                            appList = grabApps()
                            appToEdit = input("")
                            if appToEdit.lower() == "back":
                                break
                            elif all (appToEdit not in sublist[0] for sublist in appList):
                                print("[ERROR] Please Pick Existing App!")
                                time.sleep(1)
                                continue
                            print("-"  * 26)
                            print("What Would You Like To Edit? (Name, Path)")
                            print("(Back)")
                            print(" ")
                            pathOrName = str(input(""))
                            if pathOrName.lower() in ["path", "name", "back"]:
                                if pathOrName.lower() == "back":
                                    break
                                print("-" * 26)
                                print(f"What would you like the new {pathOrName.lower()} to be?")
                                print("(Back)")
                                print(" ")
                                new = input("")
                                if pathOrName.lower() == "path":
                                    try:
                                        new = Path(new.replace('"', ""))
                                        if not new.is_file():
                                            raise ValueError

                                    except (ValueError, TypeError):
                                        example = (r"C:\path\of\your\file.exe")
                                        print(f"[ERROR] File Path must lead to executable file! ({example})")
                                        time.sleep(1)
                                        continue
                                    editApp(appToEdit, "path", new)
                                elif pathOrName.lower() == "name":
                                    editApp(appToEdit, "name", new)
                                print("Changes have been saved!")
                                time.sleep(1)
                                break
                            else:
                                print('[ERROR] Input must be "path", "name", or "back"!')
                            
                            



                elif userChoice.lower() == "back":
                     break
                else:
                     print("[ERROR] Please input 1, 2, or back!")
        else:
             print("[ERROR] Please input either 1 or 2!")
             continue
                        
                          
         

if __name__ == "__main__":
    main()
