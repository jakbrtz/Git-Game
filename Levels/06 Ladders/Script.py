def InitialFile():
    return {
        "Player Location": "Ground",
        "Ladder Location": "Ground",
        "Ladder Leads To": "Nowhere",
        "Trophy Location": "Higher Platform"
    }

def GetDescription(data):

    if data["Trophy Location"] == "Player":
        return "You have the trophy. You win!"

    description = ""
    if data["Player Location"] == "Ground":
        description += "You're on the ground. \n"
        description += "There are two platforms above you, one higher than the other. \n"
        if data["Ladder Location"] == "Ground":
            description += "There's a ladder you can pick up. \n"
            if data["Ladder Leads To"] == "Lower Platform":
                description += "You can climb it to get to the Lower Platform. \n "
    elif data["Player Location"] == "Lower Platform":
        description += "You're on the lower platform. \n"
        description += "There is another platform above you. \n"
        if data["Ladder Location"] == "Lower Platform":
            description += "There's a ladder you can pick up. \n"
            if data["Ladder Leads To"] == "Highter Platform":
                description += "You can climb it to get to the Higher Platform. \n"
    else:
        description += "You're on the higher platform. \n"
        if data["Ladder Location"] == "Higher Platform":
            description += "There's a ladder you can pick up. \n"
    
    if data["Trophy Location"] == data["Player Location"]:
        description += "You can pick up the trophy. \n"
    
    if data["Ladder Location"] == "Player":
        description += "You are carrying the ladder. \n"
    
    return description

def GetActions(data):

    actions = []

    if data["Trophy Location"] == "Player":
        return actions
    
    if data["Ladder Location"] == data["Player Location"]:
        actions.append(("Pick up ladder", {"Ladder Location":"Player", "Ladder Leads To":"Nowhere"}))
    if data["Ladder Location"] == "Player":
        actions.append(("Drop Ladder", {"Ladder Location":data["Player Location"], "Ladder Leads To":"Nowhere"}))
        if data["Player Location"] == "Ground":
            actions.append(("Line up ladder with Lower Platform", {"Ladder Location":"Ground","Ladder Leads To":"Lower Platform"}))
        if data["Player Location"] == "Lower Platform":
            actions.append(("Line up ladder with Higher Platform", {"Ladder Location":"Lower Platform","Ladder Leads To":"Higher Platform"}))
       
    if data["Player Location"] == data["Ladder Location"] and data["Ladder Leads To"] != "Nowhere":
        actions.append(("Climb ladder to " + data["Ladder Leads To"], {"Player Location":data["Ladder Leads To"]}))
    if data["Player Location"] == data["Ladder Leads To"] and data["Ladder Location"] != "Player":
        actions.append(("Climb ladder to " + data["Ladder Location"], {"Player Location":data["Ladder Location"]}))

    if data["Trophy Location"] == data["Player Location"]:
        actions.append(("Pick up trophy", {"Trophy Location":"Player"}))

    return actions