import json
import os
import sys

level = "Levels/00 Sample Level"
path = level + "/SaveFile.json"

sys.dont_write_bytecode = True
sys.path.append(level)
import Script

if os.path.exists(path):
    with open(path) as f:
        data = json.load(f)
else:
    data = Script.InitialFile()
    with open(path, "w") as f:
        json.dump(data, f, indent = 4)

print(Script.GetDescription(data))
