def Help():
    print("You are a Young Hunter with the power to use a Guardian.")
    print("You are currently locked in a battle with a Vileblood who has the power to use a Dark Beast.")
    print("Defeat him to win and prevent the summoning of the Harbingers.")
    print("in battle you have the choice of Help, Check, Attack, Defend, or Wait.")
    Help_answer = raw_input("What else do you need help with?")
    if Help_answer == "Help" or Help_answer == "H":
        print("You're currently in the help section.")
    elif Help_answer == "Check" or Help_answer == "C":
        print("This allows you to check the hostile's health, status, and Ether at the cost of a turn.")
    elif Help_answer == "Attack" or Help_answer == "A":
        print("This is your attack, you have the choice of 6 attacks to use against the hostile.")
        print("Magic attacks will drain your Ether, your connection to the Moonlight Lake")
        print("But dont worry about drainging your Ether completely, you will restore some at the start of each round.")
    elif Help_answer == "Defend" or Help_answer == "D":
        print("You will have a massive defence boost for one round")
        print("But you wont be able to attack during that round")
    elif Help_answer == "Wait" or Help_answer == "W":
        print("This will make you wait a round.")
    else:
        print("I have no clue what you ment by that.")
