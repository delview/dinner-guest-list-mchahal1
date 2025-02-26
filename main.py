#TASK: Dinner Guest List

name = input("Whats your name?").capitalize().strip()

def errorfixer(number):
    while True:
        try:
            new_num = int(number)
            break
        except ValueError:
            print("Error!")
            number = input("Enter a proper, whole number.").strip()
    return new_num

def again():
    again = input("Would you like to make another dinner list?")
    if again == "y":
        dinnerlistmaker()
    if again == "n":
        print("Goodbye!")
    return

# How many guests would you like to invite
def dinnerlistmaker():
    numofguest = errorfixer(input("How many guests would you like to invite to the Dinner?".strip()))
    # Take user inputed names, add to list, loop untill finished
    guests = []
    for x in range(numofguest):
        guests.append(input("Enter a name of your guest: ").strip().capitalize())
        print("Name added!")

    # Print invitaions
    for x in guests:
        print(f"You are invited to {name}'s dinner {x}")

    # Ask to replace someone
    while True:
        choice = input("Would you like to remove someone from the invitaion list? [y] or [n]: ").strip()

        if choice == "y":
            while True:
                numofremove = errorfixer(input("How many people would you like to remove: ").strip())
                for x in range(numofremove):
                    try:
                        guests.remove(input("Who would you like to remove?").strip().capitalize())
                    except ValueError:
                        print("They are not in the dinner list!")
                        
                break
                    
            # Regenerate invitaions
            for x in guests:
                print(f"You are invited to {name}'s dinner {x}")

        elif choice == "n":
            print("Then your list is finished!")
            break
        else:
            print("enter only [y] or [n]")

    again()

dinnerlistmaker()

    

