def InitialFile():
    return {
        "Player Location": "Ground",
        "Ladder Location": "Ground",
        "Ladder Leads To": "Nowhere",
        "Trophy Location": "Higher Platform"
    }

def GetDescription(data):

    if data["Trophy Location"] == "Player":
        print("You have the trophy. You win!")
        return

    description = ""
    if data["Player Location"] == "Ground":
        print("You're on the ground.")
        print("There are two platforms above you, one higher than the other.")
        if data["Ladder Location"] == "Ground":
            print("There's a ladder you can pick up.")
            if data["Ladder Leads To"] == "Lower Platform":
                print("You can climb it to get to the Lower Platform.")
    elif data["Player Location"] == "Lower Platform":
        print("You're on the lower platform.")
        print("There is another platform above you.")
        if data["Ladder Location"] == "Lower Platform":
            print("There's a ladder you can pick up.")
            if data["Ladder Leads To"] == "Highter Platform":
                print("You can climb it to get to the Higher Platform.")
    else:
        print("You're on the higher platform.")
        if data["Ladder Location"] == "Higher Platform":
            print("There's a ladder you can pick up.")
    
    if data["Trophy Location"] == data["Player Location"]:
        print("You can pick up the trophy.")
    
    if data["Ladder Location"] == "Player":
        print("You are carrying the ladder.")
    
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