def InitialFile():
    return {
        "Door": "Locked",
        "Key Location": "Inside",
        "Player Location": "Inside"
    }

def GetDescription(data):

    if data["Player Location"] == "Outside":
        return "You've left the room. You win!"

    description = ""
    if data["Door"] == "Locked":
        description += "You're in a room with a locked door. \n"
    else:
        description += "You're in a room with an unlocked door. \n"

    if data["Key Location"] == "Inside":
        description += "There is a key on the ground. \n"
    else:
        description += "You are carrying a key. \n"

    return description

def GetActions(data):

    actions = []

    if data["Player Location"] == "Outside":
        return actions

    if data["Door"] == "Locked" and data["Key Location"] == "Player":
        actions.append(("Unlock Door", {"Door": "Unlocked"}))
    
    if data["Key Location"] == "Player":
        actions.append(("Drop Key", {"Key Location": data["Player Location"]}))
    
    if data["Key Location"] == data["Player Location"]:
        actions.append(("Pick Up Key", {"Key Location": "Player"}))
    
    if data["Door"] == "Unlocked":
        actions.append(("Leave Room", {"Player Location": "Outside"}))

    return actions