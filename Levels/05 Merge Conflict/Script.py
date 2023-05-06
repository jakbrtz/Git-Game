def InitialFile():
    return {
        "Health": "Fine",
        "Room": "Intact",
        "Dynamite": "Unexploded",
        "Dynamite Location": "Inside",
        "Player Location": "Inside"
    }

def GetDescription(data):

    if data["Player Location"] == "Outside":
        if data["Health"] == "Injured":
            return "You've left the room but you're too injured, so it doesn't count as a win."
        else:
            return "You've left the room. You win!"

    description = ""

    description += "You're inside the room. \n"
    if data["Dynamite"] == "Unexploded":
        if data["Dynamite Location"] == "Inside":
            description += "There is a dynamite on the floor. \n"
        else:
            description += "You are holding a dynamite. \n"

    if data["Room"] == "Intact":
        description += "There is a locked door preventing you from leaving. \n"
    else:
        description += "The whole room is destroyed. \n"
    
    if data["Health"] == "Sore":
        description += "Your cheek is a bit sore. \n"
    if data["Health"] == "Injured":
        description += "You're too injured to move. \n"

    return description

def GetActions(data):

    if data["Player Location"] == "Outside":
        return []

    if data["Health"] == "Injured":
        return []

    actions = []

    actions.append(("Slap yourself", {"Health": "Sore"}))

    if data["Dynamite"] == "Unexploded":
        if data["Dynamite Location"] == "Inside":
            actions.append(("Pick up Dynamite", {"Dynamite Location": "Player"}))
        else:
            actions.append(("Drop Dynamite", {"Dynamite Location": "Inside"}))
            actions.append(("Blow up door", {"Dynamite": "Exploded", "Health":"Injured","Room":"Broken"}))

    if data["Room"] == "Broken":
        actions.append(("Leave room", {"Player Location": "Outside"}))
    
    return actions