def InitialFile():
    return {
        "Red Chest": "Locked",
        "Green Chest": "Locked",
        "Blue Chest": "Locked",
        "Key": "Intact",
        "Battery Location": "Red Chest",
        "Picker Location" : "Green Chest",
        "Trophy Location" : "Blue Chest"
    }

def GetDescription(data):

    if data["Trophy Location"] == "Player":
        return "You've got the trophy. You win!"

    description = ""

    description += "There are 3 chests in front of you. \n"
    if data["Red Chest"] == "Locked":
        description += "The red chest is locked with a simple lock. \n"
    elif data["Battery Location"] == "Red Chest":
        description += "The red chest is unlocked and contains a battery. \n"
    else:
        description += "The red chest is empty. \n"
    
    if data["Green Chest"] == "Locked":
        description += "The green chest is locked with a simple lock. \n"
    elif data["Picker Location"] == "Green Chest":
        description += "The green chest is unlocked and contains a magic lock picker. \n"
    else:
        description += "The green chest is empty. \n"

    if data["Blue Chest"] == "Locked":
        description += "The blue chest is locked with a complicated lock. \n"
    elif data["Trophy Location"] == "Blue Chest":
        description += "The blue chest is unlocked and contains the trophy. \n"
    else:
        description += "The blue chest is empty. \n"
    
    if data["Battery Location"] == "Player":
        description += "You are holding a battery. \n"
    if data["Picker Location"] == "Player":
        if data["Battery Location"] == "Picker":
            description += "You are holding a powered magic lock picker. \n"
        else:
            description += "You are holding an unpowered magic lock picker. It runs on batteries. \n"

    if data["Key"] == "Intact":
        description += "You are carrying a fragile key. It will break after you use it. \n"

    return description

def GetActions(data):

    actions = []

    if data["Trophy Location"] == "Player":
        return actions

    if data["Red Chest"] == "Locked" and data["Key"] == "Intact":
        actions.append(("Unlock red chest", {"Red Chest":"Unlocked","Key":"Broken"}))
    if data["Red Chest"] == "Unlocked" and data["Battery Location"] == "Red Chest":
        actions.append(("Take battery", {"Battery Location":"Player"}))

    if data["Green Chest"] == "Locked" and data["Key"] == "Intact":
        actions.append(("Unlock green chest", {"Green Chest":"Unlocked","Key":"Broken"}))
    if data["Green Chest"] == "Unlocked" and data["Picker Location"] == "Green Chest":
        actions.append(("Take magic lock picker", {"Picker Location":"Player"}))

    if data["Blue Chest"] == "Locked" and data["Picker Location"] == "Player" and data["Battery Location"] == "Picker":
        actions.append(("Unlock blue chest", {"Blue Chest":"Unlocked","Key":"Broken"}))
    if data["Blue Chest"] == "Unlocked" and data["Trophy Location"] == "Blue Chest":
        actions.append(("Take trophy", {"Trophy Location":"Player"}))

    if data["Picker Location"] == "Player" and data["Battery Location"] == "Player":
        actions.append(("Put batter in magic lock picker", {"Battery Location":"Picker"}))

    return actions