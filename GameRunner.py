import json
import os
import sys

level = "Levels/00 Sample Level"
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
        json.dump(data, myfile, indent = 4)

print(Script.GetDescription(data))

actions = Script.GetActions(data)

for i, action in enumerate(actions):
    print(f"{i}. {action[0]}")

chosen = int(input())
for instruction in actions[chosen][1]:
    data[instruction[0]] = instruction[1]

with open(saveFilePath, "w") as myfile:
    json.dump(data, myfile, indent = 4)