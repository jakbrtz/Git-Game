import json
import os
import subprocess
import sys

# Search for Script.py
sys.path.append("")
sys.dont_write_bytecode = True
try:
    import Script
except:
    print("Script not found. ")
    print("Make sure you're in the script's directory when you open this file.")
    print("To do this, navigate to the file with the Script module and then:")
    print(" - run the `play.bat` file if one exists")
    print(" - run this file using with: python \"" + os.path.abspath(sys.argv[0]) + "\"")
    print(" - copy this file into the script's folder")
    exit()

# Load the save file, or create a new one if it doesn't exist
saveFilePath = "SaveFile.json"
if os.path.exists(saveFilePath):
    with open(saveFilePath) as myfile:
        data = json.load(myfile)
else:
    data = Script.InitialFile()
    with open(saveFilePath, "w") as myfile:
        json.dump(data, myfile, indent = 4, separators = (",\n", ": "))

# Create a git repository if it doesn't exist
if not os.path.isdir(".git"):
    subprocess.call("git init", shell=True, stdout=subprocess.DEVNULL)
    subprocess.call("git add .", shell=True, stdout=subprocess.DEVNULL)
    subprocess.call("git commit -m start", shell=True, stdout=subprocess.DEVNULL)

# The game loop:
while True:

    # Tell the user what's going on and get the list of possible actions
    print("\n\n")
    actions = Script.DescribeAndGetActions(data)
    print()

    # If no actions are available then exit
    if len(actions) == 0:
        print("No actions available")
        exit()

    # Ask the user to pick an action
    print("Available actions:")
    for i, action in enumerate(actions):
        print(f"{i}. {action[0]}")
    print()

    try:
        chosen = actions[int(input("Pick an action by entering its number: "))]
    except:
        print("Exiting...")
        exit()

    # Compare the active save file to the actual save file
    with open(saveFilePath) as myfile:
        tmpdata = json.load(myfile)
    if data != tmpdata:
        print("Save file has been edited externally. Please try again.")
        data = tmpdata
        continue

    # Update the save file
    if (callable(chosen[1])):
        data.update(chosen[1]())
    else:
        data.update(chosen[1])

    # Save the save file
    with open(saveFilePath, "w") as myfile:
        json.dump(data, myfile, indent = 4, separators = (",\n", ": "))

    # git commit the changes
    subprocess.call("git add .", shell=True, stdout=subprocess.DEVNULL)
    subprocess.call("git commit -m \"" + chosen[0] + "\"", shell=True, stdout=subprocess.DEVNULL)
