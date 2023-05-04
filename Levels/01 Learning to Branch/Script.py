def InitialFile():
    return {
        "Player Location": "Outside",
        "Entering Combination": "False",
        "Digit1": "",
        "Digit2": "",
        "Digit3": "",
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

    if (data["Entering Combination"] == "True"):
        if (data["Digit1"] == ""):
            return "What's the first digit of the combination?"
        else:
            return "What's the next digit of the combination?"

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

    if (data["Trophy Location"] == "Player"):
        return actions

    if (data["Player Location"] == "Hole"):
        return actions

    if (data["Entering Combination"] == "True"):
        if (data["Digit1"] == ""):
            digit = "Digit1"
        elif (data["Digit2"] == ""):
            digit = "Digit2"
        else:
            digit = "Digit3"
        for i in range(10):
            instructions = [(digit, str(i))]
            if digit == "Digit3":
                instructions.append(("Entering Combination", "False"))
                if data["Digit1"] == "4" and data["Digit2"] == "1" and i == 1:
                    instructions.append(("Box", "Unlocked"))
            actions.append(("Enter " + str(i), instructions))
        return actions

    if data["Box"] == "Locked":
        actions.append(("Enter combination", [("Entering Combination", "True"), ("Digit1", ""), ("Digit2", ""), ("Digit3", "")]))
    elif data["Trophy Location"] == "Box":
        actions.append(("Take Trophy", [("Trophy Location", "Player")]))

    actions.append(("Jump in hole", [("Player Location", "Hole")]))

    return actions