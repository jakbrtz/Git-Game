import json
import os
import subprocess
import sys

level = "Levels/00 Sample Level"
saveFilePath = level + "/SaveFile.json"
actionsDirectory = level + "/actions"
gitDirectory = level + "/.git"

sys.dont_write_bytecode = True
sys.path.append(level)
import Script

if os.path.exists(saveFilePath):
    with open(saveFilePath) as myfile:
        data = json.load(myfile)
else:
    data = Script.InitialFile()
    with open(saveFilePath, "w") as myfile:
        json.dump(data, myfile, indent = 4)

print(Script.GetDescription(data))
# todo: write to file?

if os.path.isdir(actionsDirectory):
    for file in os.listdir(actionsDirectory):
        os.remove(actionsDirectory + "/" + file)
else:
    os.mkdir(actionsDirectory)

for action in Script.GetActions(data):
    with open(f"{actionsDirectory}/{action[0]}.py", "a+") as myfile:
        myfile.write("import json\n")
        myfile.write("import subprocess\n")
        myfile.write("\n")
        myfile.write("with open(\"../SaveFile.json\") as myfile:\n")
        myfile.write("    data = json.load(myfile)\n")
        myfile.write("\n")
        for instruction in action[1]:
            myfile.write(f"data[\"{instruction[0]}\"] = \"{instruction[1]}\"\n")
        myfile.write("\n")
        myfile.write("with open(\"../SaveFile.json\", \"w\") as myfile:\n")
        myfile.write("    json.dump(data, myfile, indent = 4)\n")
        myfile.write("\n")
        myfile.write("subprocess.call(\"git add -u\", shell=True)\n")
        myfile.write(f"subprocess.call(\"git commit -m {action[0]}\", shell=True)\n")
        
if not os.path.isdir(gitDirectory):
    subprocess.call("git init", shell=True, cwd=level)
    subprocess.call("git add .", shell=True, cwd=level)
    subprocess.call("git commit -m start", shell=True, cwd=level)
    with open(f"{gitDirectory}/hooks/pre-commit", "a+") as myfile:
        myfile.write("#!/bin/sh\n")
        myfile.write("./test.bat\n")
    with open(f"{level}/test.bat", "a+") as myfile:
        myfile.write("# I couldn't figure out how to run python from bash\n")
        myfile.write("python ../../../../GameRunner.py\n")


subprocess.call("git add .", shell=True, cwd=level)