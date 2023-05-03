import json
import os
import sys

level = "Levels/00 Sample Level"
saveFilePath = level + "/SaveFile.json"
actionsDirectory = level + "/actions"

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
        myfile.write("\n")
        myfile.write("with open(\"../SaveFile.json\") as myfile:\n")
        myfile.write("    data = json.load(myfile)\n")
        myfile.write("\n")
        for instruction in action[1]:
            myfile.write(f"data[\"{instruction[0]}\"] = \"{instruction[1]}\"\n")
        myfile.write("\n")
        myfile.write("with open(\"../SaveFile.json\", \"w\") as myfile:\n")
        myfile.write("    json.dump(data, myfile, indent = 4)\n")