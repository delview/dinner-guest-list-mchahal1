#TASK: Dinner Guest List

name = input("Whats your name?").capitalize().strip()

def again():
    again = input("Would you like to make another dinner list?")
    if again == "y":
        dinnerlistmaker()
    if again == "n":
        print("Goodbye!")
    return

# How many guests would you like to invite
def dinnerlistmaker():
    numofguest = int(input("How many guests would you like to invite to the Dinner?".strip()))
    # Take user inputed names, add to list, loop untill finished
    guests = []
    for x in range(numofguest):
        guests.append(input("Enter a name of your guest: ").strip().capitalize())
        print("Name added!")

    # Print invitaions
    for x in guests:
        print(f"You are invited to {name}'s dinner {x}")

    # Ask to replace someone
    choice = input("Would you like to remove someone from the invitaion list?")

    if choice == "y":
        numofremove = int(input("How many people would you like to remove: ").strip())
        for x in range(numofremove):
            guests.remove(input("Who would you like to remove?").strip().capitalize())
        # Regenerate invitaions
        for x in guests:
            print(f"You are invited to {name}'s dinner {x}")

    if choice == "n":
        print("Then your list is finished!")

    again()

dinnerlistmaker()

    

