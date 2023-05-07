def InitialFile():
    return {
        "Player Location": "Outside",
        "Box": "Locked",
        "Trophy Location": "Box"
    }

def GetDescription(data):

    if (data["Trophy Location"] == "Player"):
        return "You have the trophy. You win!"

    if (data["Player Location"] == "Hole"):
        description = ""
        description += "You're at the bottom of the hole. \n"
        description += "There's a sign that says the password is 411. \n"
        description += "The hole is too deep for you to climb out. \n"
        description += "There's nothing you can do from in here. \n"
        description += "Use git to branch off from an eariler point in the story."
        return description

    description = ""
    description += "You're standing outside. \n"
    description += "There is a box with a combination lock. "
    if (data["Box"] == "Locked"):
        description += "It is locked. \n"
    else:
        description += "It is unlocked. \n"
        description += "Inside the box is a trophy. \n"
    description += "There is a hole next to you which you can jump in but it's pretty deep. \n"
    description += "There is some useful writing at the bottom of the hole, but you can't see what it says from where you are. \n"
    return description

def GetActions(data):

    actions = []

    if data["Trophy Location"] == "Player":
        return actions

    if data["Player Location"] == "Hole":
        return actions

    if data["Box"] == "Locked":
        actions.append(("Enter combination", EnterCombination))
    elif data["Trophy Location"] == "Box":
        actions.append(("Take Trophy", {"Trophy Location": "Player"}))

    actions.append(("Jump in hole", {"Player Location": "Hole"}))

    return actions

def EnterCombination():
    print("What combination do you want to try?")
    if input() == "411":
        print("Correct!")
        return {"Box":"Unlocked"}
    else:
        print("Incorrect")
        return {}
