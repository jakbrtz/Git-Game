import json
import os
import subprocess
import sys

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

saveFilePath = "SaveFile.json"

if os.path.exists(saveFilePath):
    with open(saveFilePath) as myfile:
        data = json.load(myfile)
else:
    data = Script.InitialFile()
    with open(saveFilePath, "w") as myfile:
        json.dump(data, myfile, indent = 4, separators = (",\n", ": "))

if not os.path.isdir(".git"):
    subprocess.call("git init", shell=True, stdout=subprocess.DEVNULL)
    subprocess.call("git add .", shell=True, stdout=subprocess.DEVNULL)
    subprocess.call("git commit -m start", shell=True, stdout=subprocess.DEVNULL)

while True:

    print()
    actions = Script.DescribeAndGetActions(data)
    print()
    if len(actions) == 0:
        print("No actions available")
        exit()

    gitHead1 = subprocess.check_output("git rev-parse HEAD", shell=True)

    print("Available actions:")
    for i, action in enumerate(actions):
        print(f"{i}. {action[0]}")
    print()

    try:
        chosen = actions[int(input("Pick an action by entering its number: "))]
    except:
        print("Exiting...")
        exit()

    gitHead2 = subprocess.check_output("git rev-parse HEAD", shell=True)
    if gitHead1 != gitHead2:
        print("You cannot perform an action anymore because the git head changed. Please try again. \n")
        with open(saveFilePath) as myfile:
            data = json.load(myfile)
        continue

    if (callable(chosen[1])):
        data.update(chosen[1]())
    else:
        data.update(chosen[1])

    with open(saveFilePath, "w") as myfile:
        json.dump(data, myfile, indent = 4, separators = (",\n", ": "))

    subprocess.call("git add .", shell=True, stdout=subprocess.DEVNULL)
    subprocess.call("git commit -m \"" + chosen[0] + "\"", shell=True, stdout=subprocess.DEVNULL)
