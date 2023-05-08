def InitialFile():
    return {
        "Key Location": "Table",
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
        print("You've got the trophy. You win!")
        return

    print("There are 3 chests in front of you.")
    if data["Red Chest"] == "Locked":
        print("The red chest is locked with a simple lock.")
    elif data["Battery Location"] == "Red Chest":
        print("The red chest is unlocked and contains a battery.")
    else:
        print("The red chest is empty.")
    
    if data["Green Chest"] == "Locked":
        print("The green chest is locked with a simple lock.")
    elif data["Picker Location"] == "Green Chest":
        print("The green chest is unlocked and contains a magic lock picker.")
    else:
        print("The green chest is empty.")

    if data["Blue Chest"] == "Locked":
        print("The blue chest is locked with a complicated lock.")
    elif data["Trophy Location"] == "Blue Chest":
        print("The blue chest is unlocked and contains the trophy.")
    else:
        print("The blue chest is empty.")
    
    if data["Battery Location"] == "Player":
        print("You are holding a battery.")
    if data["Picker Location"] == "Player":
        if data["Battery Location"] == "Picker":
            print("You are holding a powered magic lock picker.")
        else:
            print("You are holding an unpowered magic lock picker. It requires a battery.")

    if data["Key"] == "Intact":
        if data["Key Location"] == "Table":
            print("There is also a fragile key you can pick up.")
        else:
            print("You are carrying a fragile key. It will break after you use it.")

def GetActions(data):

    actions = []

    if data["Trophy Location"] == "Player":
        return actions
    
    if data["Key Location"] == "Table":
        actions.append(("Pick up fragile key", {"Key Location":"Player"}))

    if data["Red Chest"] == "Locked" and data["Key"] == "Intact" and data["Key Location"] == "Player":
        actions.append(("Unlock red chest", {"Red Chest":"Unlocked","Key":"Broken"}))
    if data["Red Chest"] == "Unlocked" and data["Battery Location"] == "Red Chest":
        actions.append(("Take battery", {"Battery Location":"Player"}))

    if data["Green Chest"] == "Locked" and data["Key"] == "Intact" and data["Key Location"] == "Player":
        actions.append(("Unlock green chest", {"Green Chest":"Unlocked","Key":"Broken"}))
    if data["Green Chest"] == "Unlocked" and data["Picker Location"] == "Green Chest":
        actions.append(("Take magic lock picker", {"Picker Location":"Player"}))

    if data["Blue Chest"] == "Locked" and data["Picker Location"] == "Player" and data["Battery Location"] == "Picker":
        actions.append(("Unlock blue chest", {"Blue Chest":"Unlocked","Key":"Broken"}))
    if data["Blue Chest"] == "Unlocked" and data["Trophy Location"] == "Blue Chest":
        actions.append(("Take trophy", {"Trophy Location":"Player"}))

    if data["Picker Location"] == "Player" and data["Battery Location"] == "Player":
        actions.append(("Put battery in magic lock picker", {"Battery Location":"Picker"}))

    return actions