def InitialFile():
    return {
        "Player Location": "Floor",
        "Cable Red Side": "Floor",
        "Cable Green Side": "Floor",
        "Drill Location": "Higher Platform",
        "Door": "Intact"
    }

def GetDescription(data):
    
    if data["Player Location"] == "Outside":
        return "You have left the room. You win!"
    
    description = ""

    if data["Player Location"] == "Floor":
        description += "You are standing in a room. \n"
        description += "There are two platforms above you with ladders leading to them. \n"
        description += "One platform is 5m high and the other is 6m high. \n"
    
    if data["Player Location"] == "Lower Platform":
        description += "You are on the lower platform. \n"
        if CableConnects("Lower Platform", "Higher Platform", data):
            description += "The cable is tied to the hook on this platform as well as the hook on the other platform. \n"
        elif data["Cable Red Side"] == "Lower Platform" or data["Cable Green Side"] == "Lower Platform":
            description += "The cable is tied to the hook on this platform. \n"
            if CableConnects("Player", "Lower Platform", data):
                description += "You can't climb down the ladder while holding the rope because it is tied to the hook. \n"
        else:
            description += "There is a hook where you can tie a cable to. \n"
        if data["Door"] == "Intact":
            description += "There is a locked wooden door blocking the exit. \n"
        else:
            description += "There is a hole where the door used to be. \n"
    
    if data["Player Location"] == "Higher Platform":
        description += "You are on the higher platform. \n"
        if CableConnects("Lower Platform", "Higher Platform", data):
            description += "The cable is tied to the hook on this platform as well as the hook on the other platform. \n"
        elif data["Cable Red Side"] == "Higher Platform" or data["Cable Green Side"] == "Higher Platform":
            description += "The cable is tied to the hook on this platform. \n"
            if CableConnects("Player", "Higher Platform", data):
                description += "You can't climb down the ladder while holding the rope because it is tied to the hook. \n"
        else:
            description += "There is a hook where you can tie a cable to. \n"
    
    if data["Cable Red Side"] == data["Player Location"] or data["Cable Green Side"] == data["Player Location"]:
        if data["Player Location"] == "Floor":
            description += "There is a 4m cable you can pick up. \n"
        else:
            description += "You can untie the cable. \n"
    elif data["Cable Red Side"] == "Player" or data["Cable Green Side"] == "Player":
        description += "You are carrying a cable. \n"
    
    if data["Drill Location"] == data["Player Location"]:
        description += "There is a huge drill. \n"
        description += "It is too heavy to carry. \n"
        if CableConnects("Lower Platform", "Higher Platform", data) and data["Drill Location"] == "Higher Platform":
            description += "You could hook it onto the cable. \n"

    return description

def GetActions(data):

    actions = []

    if data["Player Location"] == "Outside":
        return actions
    
    if data["Player Location"] == "Floor":
        actions.append(("Climb ladder to lower platform", {"Player Location":"Lower Platform"}))
        actions.append(("Climb ladder to higher platform", {"Player Location":"Higher Platform"}))
    
    if data["Player Location"] == "Lower Platform":
        if not CableConnects("Player", "Lower Platform", data):
            actions.append(("Climb ladder to floor", {"Player Location":"Floor"}))
        if data["Door"] == "Broken":
            actions.append(("Exit room", {"Player Location":"Outside"}))
    
    if data["Player Location"] == "Higher Platform":
        if not CableConnects("Player", "Higher Platform", data):
            actions.append(("Climb ladder to floor", {"Player Location":"Floor"}))
    
    if data["Cable Red Side"] == data["Player Location"] or data["Cable Green Side"] == data["Player Location"]:
        pickupcableinstruction = {}
        if data["Cable Red Side"] == data["Player Location"]:
            pickupcableinstruction["Cable Red Side"] = "Player"
        if data["Cable Green Side"] == data["Player Location"]:
            pickupcableinstruction["Cable Green Side"] = "Player"
        actions.append(("Pick up cable" if data["Player Location"] == "Floor" else "Untie cable", pickupcableinstruction))
    if data["Cable Red Side"] == "Player":
        actions.append(("Drop red side of cable" if data["Player Location"] == "Floor" else "Tie red side of cable to hook", {"Cable Red Side": data["Player Location"]}))
    if data["Cable Green Side"] == "Player":
        actions.append(("Drop green side of cable" if data["Player Location"] == "Floor" else "Tie green side of cable to hook", {"Cable Green Side": data["Player Location"]}))
    
    if data["Drill Location"] == data["Player Location"]:
        if CableConnects("Lower Platform", "Higher Platform", data) and data["Drill Location"] == "Higher Platform":
            actions.append(("Put massive drill on cable", PutDrillOnZipline))
        if data["Drill Location"] == "Lower Platform" and data["Door"] == "Intact":
            actions.append(("Drill massive hole in door", {"Door":"Broken"}))
    
    return actions

def CableConnects(item1, item2, data):
    return (data["Cable Red Side"] == item1 and data["Cable Green Side"] == item2) or (data["Cable Red Side"] == item2 and data["Cable Green Side"] == item1)

def PutDrillOnZipline():
    print("The massive drill swings down the zipline. Look at it go!")
    print("It lands safely on the lower platform.")
    return {"Drill Location":"Lower Platform"}

# Yea there's probably some edge case about holding the rope while it's already tied to another room
# I don't feel like dealing with that, mostly because I know I'm going to rewrite everything soon