def InitialFile():
    return {
        "Health": "Fine",
        "Room": "Intact",
        "Dynamite": "Unexploded",
        "Dynamite Location": "Inside",
        "Player Location": "Inside"
    }

def DescribeAndGetActions(data):

    if data["Player Location"] == "Outside":
        if data["Health"] == "Injured":
            print("You've left the room but you're too injured, so it doesn't count as a win.")
        else:
            print("You've left the room. You win!")
        return []

    actions = []
    actions.append(("Slap yourself", {"Health": "Sore"}))

    print("You're inside the room.")
    if data["Dynamite"] == "Unexploded":
        if data["Dynamite Location"] == "Inside":
            print("There is a dynamite on the floor.")
            actions.append(("Pick up Dynamite", {"Dynamite Location": "Player"}))
        else:
            print("You are holding a dynamite.")
            actions.append(("Drop Dynamite", {"Dynamite Location": "Inside"}))
            actions.append(("Blow up door", {"Dynamite": "Exploded", "Health":"Injured","Room":"Broken"}))

    if data["Room"] == "Intact":
        print("There is a locked door preventing you from leaving.")
    else:
        print("The whole room is destroyed.")
        actions.append(("Leave room", {"Player Location": "Outside"}))
    
    if data["Health"] == "Sore":
        print("Your cheek is a bit sore.")
    if data["Health"] == "Injured":
        print("You're too injured to move.")
        return []

    return actions