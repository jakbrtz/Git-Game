def InitialFile():
    return {
        "Player Location": "Outside",
        "Box": "Locked",
        "Trophy Location": "Box"
    }

def DescribeAndGetActions(data):

    if (data["Trophy Location"] == "Player"):
        print("You have the trophy. You win!")
        return []

    if (data["Player Location"] == "Hole"):
        print("You're at the bottom of the hole.")
        print("There's a sign that says the password is 411.")
        print("The hole is too deep for you to climb out.")
        print("There's nothing you can do from in here.")
        print("Use git to branch off from an eariler point in the story.")
        return []

    actions = []
    print("You're standing outside.")
    print("There is a box with a combination lock.")
    if (data["Box"] == "Locked"):
        print("It is locked.")
        actions.append(("Enter combination", EnterCombination))
    else:
        print("It is unlocked.")
        if data["Trophy Location"] == "Box":
            print("Inside the box is a trophy.")
            actions.append(("Take Trophy", {"Trophy Location": "Player"}))
    print("There is a hole next to you which you can jump in but it's pretty deep.")
    print("There is some useful writing at the bottom of the hole, but you can't see what it says from where you are.")
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
