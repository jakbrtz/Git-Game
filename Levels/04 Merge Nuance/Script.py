def InitialFile():
    return {
        "Axe Location": "Room 1",
        "Player Location": "Room 1",
        "Room 1 door": "Intact",
        "Room 2 door": "Intact"
    }

def GetDescription(data):

    if data["Player Location"] == "Outside":
        return "You've left the rooms. You win!"
    
    description = ""

    if data["Player Location"] == "Room 1":
        description += "You're standing in the first room. \n"
        if data["Room 1 door"] == "Intact":
            description += "There is a locked wooden door preventing you from going to the next room. \n"
        else:
            description += "There is a door frame you could walk through to get to the next room. \n"
    
    if data["Player Location"] == "Room 2":
        description += "You're standing in the second room. \n"
        description += "There is an open door frame leading back to the first room. \n"
        description += "There is a ladder leading up to an elevated platform which has a door leading to the exit. \n"
        if data["Axe Location"] == "Player":
            description += "You cannot climb the ladder while carrying the axe. \n"

    if data["Player Location"] == "Room 2 Platform":
        description += "You're standing on the platform in the second room. \n"
        if data["Room 2 door"] == "Intact":
            description += "There is a locked wooden door preventing you from exiting. \n"
        else:
            description += "There is a door frame you could walk through to get to exit. \n"
    
    if data["Axe Location"] == "Player":
        description += "You are carrying an axe. \n"
    elif data["Axe Location"] == data["Player Location"]:
        description += "There is an axe on the floor you can pick up. \n"

    return description

def GetActions(data):

    actions = []

    if data["Player Location"] == "Outside":
        return actions
    
    if data["Player Location"] == "Room 1":
        if data["Room 1 door"] == "Broken":
            actions.append(("Go to second room", {"Player Location":"Room 2"}))
        elif data["Axe Location"] == "Player":
            actions.append(("Break door", {"Room 1 door":"Broken"}))
            
    
    if data["Player Location"] == "Room 2":
        actions.append(("Go to first room", {"Player Location":"Room 1"}))
        if data["Axe Location"] != "Player":
            actions.append(("Climb ladder", {"Player Location":"Room 2 Platform"}))

    if data["Player Location"] == "Room 2 Platform":
        if data["Room 2 door"] == "Broken":
            actions.append(("Leave room", {"Player Location":"Outside"}))
        elif data["Axe Location"] == "Player":
            actions.append(("Break door", {"Room 2 door":"Broken"}))

    if data["Axe Location"] == "Player":
        actions.append(("Drop Axe", {"Axe Location": data["Player Location"]}))
    if data["Axe Location"] == data["Player Location"]:
        actions.append(("Pick Up Axe", {"Axe Location": "Player"}))
    
    return actions