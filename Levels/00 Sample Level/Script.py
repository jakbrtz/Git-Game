import json

with open("SaveFile.json") as f:
    data = json.load(f)

description = ""
if (data["Player Location"] == "Outside"):
    description += "You've left the room. You win!"
    quit()
else:
    if (data["Door"] == "Locked"):
        description += "You're in a room with a locked door. \n"
    else:
        description += "You're in a room with an unlocked door. \n"

    if (data["Key Location"] == "Inside"):
        description += "There is a key on the ground. \n"
    else:
        description += "You are carrying a key. \n"

    if (data["Door"] == "Locked" and data["Key Location"] == "Player"):
        # unlock door
        pass
    
    if (data["Key Location"] == "Player"):
        # drop key
        pass
    
    if (data["Key Location"] == data["Player Location"]):
        # pick up key
        pass
    
    if (data["Door"] == "Unlocked"):
        # go outside
        pass

print(description)

#with open("sample.json", "w") as outfile:
#    json.dump(data, outfile, indent = 4)