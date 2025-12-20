# ============================================================
#   FAKE NEWS HEADLINE GENERATOR - PYTHON PROJECT
#   Author: Shaikh Mubarish GT
#   Created By: Shaikh Mubarish
#   Written With ❤️ by Mubarish
#   Version: 2.0 (Upgraded Edition).
# ============================================================

import random
import os
import time

# ------------------------------------------------------------
# Lists Created & Curated By: Shaikh Mubarish
# ------------------------------------------------------------

subjects = [
    "Shahrukh Khan",
    "AKSHAY KUMMAAR"
    "Virat Kohli",
    "Salmaan Khan",
    "Nirmala Sitharaman",
    "Mahesh Babu"
    "allu artjun"
    "A Mumbai Cat",
    "Group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi",
    "A Scared Software Engineer",
    "A Confused Python Coder"
    "amitab bachan"
]

actions = [
    "Launches",
    "Cancels",
    "shaadi"
    "Dances with",
    'going to ghatkoper'
    "Eats",
    "Declares war on",
    "Orders 100 plates of",
    "sai road"
    "Starts crying over",
    "Becomes best friends with"
    'Becomes Hydrabadi'
    "latur golai",
    "laufhter chef",
    "cocsit colloge"
    "reading "
    "come to latur",
    "dubie burj"
    "Latur ki public bolti"
]

place_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "at Sai Road, Latur",
    "near Taj Mahal",
    "enter the bigboss house",
    "enter the reading room"
    "motu patlu ki jodi"
    "during IPL Match",
    "inside Parliament",
    "on a flying helicopter",
    "while stuck in traffic"
]

endings = [
    "— Public shocked!",
    "_everyone is dancing"
    "— Internet can't handle this!",
    "— Social media on fire! 🔥",
    "— Experts have no explanation 🤯",
    "— Fans celebrating worldwide 🎉",
    "— Nation wants to know more!"
]

emojis = ["😂", "😳", "🔥", "🤣", "💥", "😱", "🤡", "🥳", "🫡"]


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# MAIN PROGRAM LOOP
while True:
    clear_screen()

    print("==============================================")
    print("        📰 FAKE NEWS HEADLINE GENERATOR        ")
    print("==============================================")
    print("              Author: Shaikh Mubarish         ")
    print("==============================================")

    sub = random.choice(subjects)
    act = random.choice(actions)
    pot = random.choice(place_or_things)
    end = random.choice(endings)
    emoji = random.choice(emojis)

    headline = f"\nBREAKING NEWS: {sub} {act} {pot}! {end} {emoji}"
    print(headline)

    user_input = input("\nDo you want another headline? (y/n): ").strip().lower()
    if user_input == "n":
        break

print("\nTHANK YOU FOR USING THE FAKE NEWS GENERATOR! 🎯")
print("Created By: Shaikh Mubarish GT\n")
