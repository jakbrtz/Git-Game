def InitialFile():
    return {
        "Axe Location": "Room 1",
        "Player Location": "Room 1",
        "Room 1 door": "Intact",
        "Room 2 door": "Intact"
    }

def DescribeAndGetActions(data):

    actions = []

    if data["Player Location"] == "Outside":
        print("You've left the rooms. You win!")
        return []
    
    if data["Player Location"] == "Room 1":
        print("You're standing in the first room.")
        if data["Room 1 door"] == "Intact":
            print("There is a locked wooden door preventing you from going to the next room.")
            if data["Axe Location"] == "Player":
                actions.append(("Break door", {"Room 1 door":"Broken"}))
        else:
            print("There is a door frame you could walk through to get to the next room.")
            actions.append(("Go to second room", {"Player Location":"Room 2"}))
    
    if data["Player Location"] == "Room 2":
        print("You're standing in the second room.")
        print("There is an open door frame leading back to the first room.")
        print("There is a ladder leading up to an elevated platform which has a door leading to the exit.")
        actions.append(("Go to first room", {"Player Location":"Room 1"}))
        if data["Axe Location"] == "Player":
            print("You cannot climb the ladder while carrying the axe.")
        else:
            actions.append(("Climb ladder", {"Player Location":"Room 2 Platform"}))

    if data["Player Location"] == "Room 2 Platform":
        print("You're standing on the platform in the second room.")
        if data["Room 2 door"] == "Intact":
            print("There is a locked wooden door preventing you from exiting.")
            if data["Axe Location"] == "Player":
                actions.append(("Break door", {"Room 2 door":"Broken"}))
        else:
            print("There is a door frame you could walk through to get to exit.")
            actions.append(("Leave room", {"Player Location":"Outside"}))
    
    if data["Axe Location"] == "Player":
        print("You are carrying an axe.")
        actions.append(("Drop Axe", {"Axe Location": data["Player Location"]}))
    elif data["Axe Location"] == data["Player Location"]:
        print("There is an axe on the floor you can pick up.")
        actions.append(("Pick Up Axe", {"Axe Location": "Player"}))

    return actions