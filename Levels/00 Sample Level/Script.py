def InitialFile():
    return {
        "Door": "Locked",
        "Key Location": "Inside",
        "Player Location": "Inside"
    }

def DescribeAndGetActions(data):

    if data["Player Location"] == "Outside":
        print("You've left the room. You win!")
        return []

    actions = []

    if data["Door"] == "Locked":
        print("You're in a room with a locked door.")
    else:
        print("You're in a room with an unlocked door.")
        actions.append(("Leave Room", {"Player Location": "Outside"}))

    if data["Key Location"] == "Inside":
        print("There is a key on the ground.")
        actions.append(("Pick Up Key", {"Key Location": "Player"}))
    else:
        print("You are carrying a key.")
        actions.append(("Drop Key", {"Key Location": "Inside"}))

    if data["Door"] == "Locked" and data["Key Location"] == "Player":
        actions.append(("Unlock Door", {"Door": "Unlocked"}))
    
    return actions