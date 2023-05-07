import json
import os
import subprocess
import sys

level = "Levels/07 Teleportation"
saveFilePath = level + "/SaveFile.json"

sys.dont_write_bytecode = True
sys.path.append(level)
import Script

if os.path.exists(saveFilePath):
    with open(saveFilePath) as myfile:
        data = json.load(myfile)
else:
    data = Script.InitialFile()
    with open(saveFilePath, "w") as myfile:
        json.dump(data, myfile, indent = 4, separators = (",\n", ": "))

if not os.path.isdir(level + "/.git"):
    subprocess.call("git init", shell=True, cwd=level, stdout=subprocess.DEVNULL)
    subprocess.call("git add .", shell=True, cwd=level, stdout=subprocess.DEVNULL)
    subprocess.call("git commit -m start", shell=True, cwd=level, stdout=subprocess.DEVNULL)

while True:

    print(Script.GetDescription(data))

    actions = Script.GetActions(data)

    if len(actions) == 0:
        exit()

    for i, action in enumerate(actions):
        print(f"{i}. {action[0]}")

    gitHead1 = subprocess.check_output("git rev-parse HEAD", shell=True, cwd=level)

    chosen = actions[int(input())]
    if (callable(chosen[1])):
        data.update(chosen[1]())
    else:
        data.update(chosen[1])
    print()

    gitHead2 = subprocess.check_output("git rev-parse HEAD", shell=True, cwd=level)

    if gitHead1 != gitHead2:
        print("You cannot perform an action anymore because the git head changed. Please try again. \n")
        with open(saveFilePath) as myfile:
            data = json.load(myfile)
        continue

    with open(saveFilePath, "w") as myfile:
        json.dump(data, myfile, indent = 4, separators = (",\n", ": "))

    subprocess.call("git add .", shell=True, cwd=level, stdout=subprocess.DEVNULL)
    subprocess.call("git commit -m \"" + chosen[0] + "\"", shell=True, cwd=level, stdout=subprocess.DEVNULL)
