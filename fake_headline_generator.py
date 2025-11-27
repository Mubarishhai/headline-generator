
#    — Author: Shaikh Mubarish gt
import random

# list of subjects
subjects = [
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A Mumbai Cat",
    "Group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw driver from Delhi"
]

# list of actions
actions = [
    "Launches",
    "Cancels",
    "Dances with",
    "Eats",
    "Declares war on",
    "Orders",
    "Celebrates"
]

# list of places/things
place_or_things = [
    "at Red Fort",
    "in Mumbai local train",
    "at Sai Road, Latur",
    "near Taj Mahal",
    "during IPL match",
    "inside Parliament"
]

# Loop
while True:

    sub = random.choice(subjects)
    act = random.choice(actions)
    pot = random.choice(place_or_things)

    headline = f"BREAKING NEWS: {sub} {act} {pot}"
    print("\n" + headline)

    user_input = input("\nDo you wish to continue? (y/n): ").strip().lower()
    if user_input == "n":
        break

print("\nTHANKS FOR USING THE FAKE NEWS HEADLINE GENERATOR\n")
