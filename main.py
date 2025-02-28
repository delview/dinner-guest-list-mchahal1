#TASK: Dinner Guest List

def errorfixer(number): # handles any str into int errors
    while True:
        try:
            new_num = int(number) #trys to make the inputed num into a int
            break
        except ValueError: # if it does not work, asks for a new num and loops again
            print("Error!")
            number = input("Enter a proper, whole number.").strip()
    return new_num # returns working num

def again(): # asks to play again
    while True:
        again = input("Would you like to make another dinner list? [y] or [n]")
        if again == "y": # if they want to play, runs the game again
            dinnerlistmaker()
        elif again == "n": # otherwise, returns to end of code and ends game
            print("Goodbye!")
            break
        else:
            print("enter only [y] or [n]")
    return

def dinnerlistmaker(): # Main program
    # asks How many guests you would like to invite
    numofguest = errorfixer(input("How many guests would you like to invite to the Dinner? ".strip()))
    # Take user inputed names, adds to list
    guests = []
    for x in range(numofguest): # loops until numofguest is finished
        guests.append(input("Enter a name of your guest: ").capitalize())
        print("Name added!")

    guests = sorted(guests) # sorts guest list 
    # Print invitaions
    for x in guests: # prints all the invitations
        print(f"You are invited to {name}'s dinner {x}!")

    # Ask to replace someone loop
    while True:
        choice = input("Would you like to remove someone from the invitaion list? [y] or [n]: ").strip() # Asks if user wants to remove a name from the list
        
        if choice == "y":
            while True:
                numofremove = errorfixer(input("How many people would you like to remove: ").strip())
                for x in range(numofremove): # loops however much the user entered 
                    removedname = input("Who would you like to remove? ").strip().capitalize()
                    if removedname in guests: # checks if the removed name is in the guest list
                        guests.remove(removedname) # removes the name
                        print(f"{removedname} has been removed from the list!")
                    else: # if not in list, breaks out of smaller loop back into intial choice
                        print("They are not in the dinner list!")
                        break
                break

            # Regenerate invitaions
            print("Here is your dinner list:")
            for x in guests:
                print(f"You are invited to {name}'s dinner {x}!")

        elif choice == "n":
            print("Then your list is finished!")
            break # breaks out of remove loop and goes to "again()" function
        else:
            print("enter only [y] or [n]")

    again() #runs function that asks if they want to make another list

name = input("Whats your name?").capitalize().strip()
dinnerlistmaker() # Starts the dinner guest list maker
