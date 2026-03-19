# Giant Treasure Adventure

# Step 1: Create your hero
name = input("What is your hero's name? ")
age = int(input("How old is your hero? "))
gold = 10  # starting gold
has_sword = False  # boolean variable

print(f"\nWelcome, {name}! You are {age} years old and start with {gold} gold coins.")

# Step 2: Choose a path
path = input("Do you want to go into the (cave) or walk into the (forest)? ").lower()

if path == "cave":
    print("\nYou enter the dark cave...")
    has_sword = True
    print("You found a shiny sword! 🗡️")
elif path == "forest":
    print("\nThe forest is quiet... too quiet.")
    gold += 5
    print("You found 5 gold coins hidden under a rock! 💰")

# Step 3: Face the giant
print("\nOh no! A giant appears! 🐉")

if has_sword:
    print(f"{name} bravely fights the giant with the sword...")
    print("You WIN! The giant flees, and you keep your treasure.")
else:
    if gold >= 15:
        print(f"{name} throws gold at the giant until it gets bored... You escape!")
    else:
        print(f"{name} has no sword and not enough gold. The giant steps on you. 🔥 Game Over.")

# Step 4: End of game summary
print(f"\nGame Over! {name} ends the adventure with {gold} gold coins.")