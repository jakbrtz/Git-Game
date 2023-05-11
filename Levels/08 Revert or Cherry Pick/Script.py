def InitialFile():
    return {
        "Door1": "Locked",
        "Door2": "Locked",
        "Key Location": "Room1",
        "Key":"Intact",
        "Player Location": "Room1"
    }

def DescribeAndGetActions(data):

    if data["Player Location"] == "Outside":
        print("You've left the room. You win!")
        return []

    actions = []

    if data["Player Location"] == "Room1":
        print("You're in the first room. ")
        if data["Door1"] == "Locked":
            print("There is a locked door leading to the second room.")
            if data["Key"] == "Intact" and data["Key Location"] == "Player":
                actions.append(("Unlock door", {"Key":"Broken","Door1":"Unlocked"}))
        else:
            print("The door to the second room is open.")
            actions.append(("Go to second room", {"Player Location":"Room2"}))

    if data["Player Location"] == "Room2":
        print("You're in the second room. ")
        actions.append(("Go to first room", {"Player Location":"Room1"}))
        if data["Door2"] == "Locked":
            print("There is a locked door leading to the exit.")
            if data["Key"] == "Intact" and data["Key Location"] == "Player":
                actions.append(("Unlock door", {"Key":"Broken","Door2":"Unlocked"}))
        else:
            print("The door to the exit is open.")
            actions.append(("Go to exit", {"Player Location":"Outside"}))
        
    if data["Key"] == "Intact":
        if data["Key Location"] == "Player":
            print("You are holding a fragile key. It will break after you use it. ")
            actions.append(("Drop key", {"Key Location":data["Player Location"]}))
        elif data["Key Location"] == data["Player Location"]:
            print("There is a fragile key on the floor. ")
            actions.append(("Pick up key", {"Key Location":"Player"}))

    return actions