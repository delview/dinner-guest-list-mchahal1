#TASK: Dinner Guest List

name = input("Whats your name?").capitalize().strip()
# How many guests would you like to invite
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
    guests.remove(input("Who would you like to remove?"))
# Regenerate invitaions