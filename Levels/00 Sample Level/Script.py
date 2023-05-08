def InitialFile():
    return {
        "Door": "Locked",
        "Key Location": "Inside",
        "Player Location": "Inside"
    }

def GetDescription(data):

    if data["Player Location"] == "Outside":
        print("You've left the room. You win!")
        return

    if data["Door"] == "Locked":
        print("You're in a room with a locked door.")
    else:
        print("You're in a room with an unlocked door.")

    if data["Key Location"] == "Inside":
        print("There is a key on the ground.")
    else:
        print("You are carrying a key.")

    print()

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