import random

# The player starts with 2 hearts
hearts = 2
# Track the number of coaches met
coaches_met = 0

def check_coaches(coaches_met): # variable
    if coaches_met == 2:
        print("Met 2 coaches! You won the game! End of level 1 🚀")
        exit()

def heart_check(hearts):
    if hearts == 0:
        print("Out of hearts 💔, game over! ")
        exit()


    # compare variable to winning number of coaches

    # if greater than (we win), end the game

    # else, do nothing

# Start the game function
def start_game():
    # Print the instructions and welcome message
    print("Oh hey!! Welcome to Heart of the Rainforest.")
    print("Brought to you by: Moumita, Obi, and Isa – the dream team!")
    print("Your Goals: Escape the rainforest and meet 2 coaches. Easy peasy, right? 😎")
   
    forest_entrance(coaches_met, hearts)

# Scene 1: Forest Entrance
def forest_entrance(coaches_met, hearts):
    print("Level 1: You’re at the rainforest entrance. Trees everywhere. Smells like adventure.")
    print(f"Hearts: {hearts} 🤍")
    choice = input("Options: 'go north', 'look around', 'go south', 'restart', 'quit': ")

    # Make the choices
    if choice == "go north":
        print("You met a coach, that’s pretty cool! Now get ready to rule!")
        # The user meets a coach here
        coaches_met = meet_coach(coaches_met)
        
        # Check if player has won
        check_coaches(coaches_met)
            
        # Move to the next scene if they haven't won
        cave_of_echos(coaches_met, hearts)
    
    elif choice == "look around":
        print("You look around and someone’s side-eyeing you for playing games instead of studying. Oops. 🙃")
        forest_entrance(coaches_met, hearts)

    elif choice == "go south":
        print("You trip over a vine and the mushroom laughs. That's tough.")
        hearts -= 1
        print(f"Hearts: {hearts} 🤍")
        
        # Check if hearts are depleted
        heart_check(hearts)
        
        # The user meets a coach if they haven't lost all hearts
        coaches_met = meet_coach(coaches_met)
        
        # Check win condition
        check_coaches(coaches_met)
        
        # Move to the next scene if they haven't won
        cave_of_echos(coaches_met, hearts)

    elif choice == "restart":
        print("Restarting the game!")
        start_game()

    elif choice == "quit":
        print("Goodbye! Thanks for playing.")
        return

    else:
        print("Not an option! Try again.")
        forest_entrance(coaches_met, hearts)

#Scene 2: Cave of Echoes
def cave_of_echos(coaches_met, hearts):
    print("You’re in front of a Cave. 'CAUTION: don't go in there' A rock exclaimed. What do you wanna do? ")
    print(f"Hearts: {hearts} 🤍")

    # Options for the player in this scene
    choice = input("Options: 'shout', 'walk', 'cry', 'restart', 'quit': ")

    if choice == "shout":
        print("You shout at the cave and it shouts back with 'YAHAHOO' booo 👎")
        hearts -= 1
        print(f"Hearts: {hearts} 🤍")
        
        # Check if hearts are depleted
        heart_check(hearts)
        cave_of_echos(coaches_met, hearts)  # Go back to the same scene if not over

    elif choice == "walk":
        print("You walk ahead and see a coach waving at you!🔥 ")
        coaches_met = meet_coach(coaches_met)
        
        # Check win condition
        check_coaches(coaches_met)
        # Continue exploring the cave if they haven't won
        cave_of_echos(coaches_met, hearts)

    elif choice == "cry":
        print("You cry out loud but no one is here to help you...")
        hearts -= 1
        print(f"Hearts: {hearts} 🤍")

        # Check if hearts are depleted
        heart_check(hearts)
        cave_of_echos(coaches_met, hearts)  # Return to forest entrance if not over

    elif choice == "restart":
        print("Restarting the game!")
        start_game()

    elif choice == "quit":
        print("Goodbye! Thanks for playing.")
        return

    else:
        print("Not an option! Try again.")
        cave_of_echos(coaches_met, hearts)

# Function to meet a coach
def meet_coach(coaches_met):
    coaches = ["Coach Asim", "Coach Naomi", "Coach Norma", "Coach Sadeem", "Coach Nando", "Coach Holly"]
    coach = random.choice(coaches)
    
    # Only allow meeting a coach if they haven't met 2 already
    if coaches_met < 2:
        print(f"You met {coach}!")
        if coach == "Coach Asim":
            print(f"{coach}: 'IDK how you got here but let's get you out of here.'")
        elif coach == "Coach Naomi":
            print(f"{coach}: 'You struggled a lot champ, now let's go get some food 🥙'")
        elif coach == "Coach Norma":
            print(f"{coach}: 'I'm trying to get out of this cave so let me just call my private jet!'")
        elif coach == "Coach Sadeem":
            print(f"{coach}: 'Give me your elevator pitch right now if you want to get out of this cave '")
        elif coach == "Coach Nando":
            print(f"{coach}: 'Oh my this would be so fun if all the kids from CodeNext come here and experience it!'")
        elif coach == "Coach Holly":
            print(f"{coach}: 'Let's brainstorm ways to create a Mobility Lab here 🤔'")
        coaches_met += 1
    else:
        print(f"{coach} says: Keep it up!")
    
    return coaches_met

# Start the game
start_game()
