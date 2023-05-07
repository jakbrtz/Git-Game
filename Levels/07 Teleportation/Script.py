def InitialFile():
    return {
        "Player Location": "Attic",
        "Key Location": "Green Room",
        "Door": "Locked"
    }

def GetDescription(data):

    if data["Player Location"] == "Outside":
        return "You've left the room. You win!"

    description = ""
    if data["Player Location"] == "Attic":
        description += "You're in the attic. There are two holes you can jump into. \n"
        description += "One leads to the green room, the other hole leads to the blue room. \n"
    
    if data["Player Location"] == "Green Room":
        description += "You're in the green room. \n"
    
    if data["Player Location"] == "Blue Room":
        description += "You're in the blue room. \n"
        if data["Door"] == "Locked":
            description += "There is a locked door. \n"
        else:
            description += "There is an unlocked door leading out. \n"
    
    if data["Key Location"] == "Player":
        description += "You are holding a key. \n"
    if data["Key Location"] == data["Player Location"]:
        description += "There is a key on the ground you can pick up. \n"
    
    return description

def GetActions(data):

    actions = []

    if data["Player Location"] == "Outside":
        return actions

    if data["Player Location"] == "Attic":
        actions.append(("Go to Green Room", {"Player Location":"Green Room"}))
        actions.append(("Go to Blue Room", {"Player Location":"Blue Room"}))
    
    if data["Player Location"] == "Blue Room":
        if data["Door"] == "Unlocked":
            actions.append(("Leave the room", {"Player Location":"Outside"}))
        elif data["Key Location"] == "Player":
            actions.append(("Unlock door", {"Door":"Unlocked"}))
    
    if data["Key Location"] == "Player":
        actions.append(("Drop key", {"Key Location":data["Player Location"]}))
    if data["Key Location"] == data["Player Location"]:
        actions.append(("Pick up key", {"Key Location":"Player"}))

    return actions