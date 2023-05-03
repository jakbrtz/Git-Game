import json
import subprocess

with open("../SaveFile.json") as myfile:
    data = json.load(myfile)

data["Key Location"] = "Player"

with open("../SaveFile.json", "w") as myfile:
    json.dump(data, myfile, indent = 4)

subprocess.call("git add -u", shell=True)
subprocess.call("git commit -m PickUpKey", shell=True)
