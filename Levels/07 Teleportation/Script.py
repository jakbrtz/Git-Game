def InitialFile():
    return {
        "Player Location": "Attic",
        "Key Location": "Green Room",
        "Door": "Locked"
    }

def GetDescription(data):

    if data["Player Location"] == "Outside":
        print("You've left the room. You win!")
        return

    if data["Player Location"] == "Attic":
        print("You're in the attic. There are two holes you can jump into.")
        print("One leads to the green room, the other hole leads to the blue room.")
    
    if data["Player Location"] == "Green Room":
        print("You're in the green room.")
    
    if data["Player Location"] == "Blue Room":
        print("You're in the blue room.")
        if data["Door"] == "Locked":
            print("There is a locked door.")
        else:
            print("There is an unlocked door leading out.")
    
    if data["Key Location"] == "Player":
        print("You are holding a key.")
    if data["Key Location"] == data["Player Location"]:
        print("There is a key on the ground you can pick up.")
    
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