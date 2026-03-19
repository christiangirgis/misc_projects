"""
Break the Brainrot 🧠🚫
Practice: VARIABLES, CONDITIONS, LOOPS

Win goal:
- Build enough FOCUS before you run out of time.
- Keep SCROLL (doomscroll meter) from getting too high.

Scripture: Philippians 4:8 — Think about what is true, noble, right, pure, lovely, admirable.
"""

import random
import textwrap

def wrap(s):
    return textwrap.fill(s, width=78)

def intro():
    print("="*78)
    print("🧠 BREAK THE BRAINROT – A Friendly After-School Adventure")
    print("="*78)
    print(wrap(
        "It's after school, and your phone is tempting you with endless shorts and memes. "
        "Your goal is to avoid the 'brainrot spiral' by making wise choices before youth "
        "group starts. Build your FOCUS by doing healthy, faith-filled activities, keep "
        "SCROLL low, and arrive ready to shine your light! (Matthew 5:16)"
    ))
    print("-"*78)
    print("Controls: choose a letter and press Enter.")
    print("  W = Watch one short (risky)   H = Healthy break (water/stretch)")
    print("  S = Scripture/Prayer          F = Help a Friend")
    print("  I = Status/Inventory          Q = Quit")
    print("-"*78)

def status(focus, scroll, minutes, inventory):
    print("-"*78)
    # ERROR 1
    print(f"Time: {minutes} min | Focus: {focus} | Scroll: {scroll} | Inventory: {inventory}")
    print("-"*78)

def random_event(focus, scroll, inventory):
    """Small chance events after each action."""
    events = [
        "funny-llama",
        "youth-group-text",
        "pop-quiz-memory",
        "ad-storm",
        "neighbor-smile",
    ]
    e = random.choice(events)

    if e == "funny-llama":
        print(wrap("You remember a hilarious llama meme. You giggle, but it nibbles at your focus."))
        scroll += 1
        focus = max(0, focus - 1)
    elif e == "youth-group-text":
        print(wrap("A friend texts: 'See you at youth group! Bring good vibes.' You feel encouraged."))
        focus += 1
    elif e == "pop-quiz-memory":
        print(wrap("You recall a verse from last week: 'Let your light shine.' Confidence rises."))
        focus += 2
    elif e == "ad-storm":
        print(wrap("Ad storm! Skip… skip… skip… it’s a bit draining."))
        scroll += 1
    elif e == "neighbor-smile":
        print(wrap("You smile at a neighbor. They smile back. Small kindness, big lift."))
        focus += 1

    return focus, scroll, inventory

def healthy_break(focus, scroll, inventory):
    print(wrap("Healthy break menu: [A] drink water, [B] stretch, [C] 30-second walk"))
    choice = input("Choose A/B/C: ").strip().upper()
    if choice == "A":
        print("You chug water. Hydration helps your brain.")
        focus += 2
        inventory.append("empty-bottle")
    elif choice == "B":
        print("You stretch your shoulders and neck. Ahh… tension fades.")
        focus += 1
    elif choice == "C":
        print("You walk a quick lap and breathe.")
        # For-loop demo: 3 calm breaths
        for count in range(3, 0, -1):
            print(f"Inhale… exhale… {count}")
        focus += 2
        scroll = max(0, scroll - 1)
    else:
        print("You hesitate and end up doing nothing.")
    return focus, scroll, inventory

def scripture_prayer(focus, used_prayer):
    if used_prayer:
        print("You already prayed once—now walk in that peace. 🙏")
        return focus, used_prayer
    print(wrap("You pause and pray: 'Lord, help me fix my thoughts on what is true and noble.'"))
    verse = "Philippians 4:8"
    print(f"Scripture boost from {verse}! 🕊️")
    focus += 3
    used_prayer = True
    return focus, used_prayer

def help_friend(focus, scroll):
    print(wrap("A friend is stuck on homework. You could explain the main idea or share a tip."))
    tip_bank = [
        "Try chunking the instructions.",
        "Underline the verbs in the question.",
        "Check the example problem first.",
    ]
    # For-loop demo: show tips nicely
    for i, tip in enumerate(tip_bank, start=1):
        print(f"  Tip {i}: {tip}")
    print(wrap("They say thanks! Serving others helps you too."))
    focus += 2
    scroll = max(0, scroll - 1)
    return focus, scroll

def watch_short(focus, scroll):
    print(wrap("You open one short. Will it be harmless or a brainrot rabbit hole?"))
    roll = random.randint(1, 6)
    if roll <= 2:
        print("It was a wholesome craft hack. Not bad!")
        focus += 1
    elif roll <= 4:
        print("Meh—kind of mindless. You lose some focus.")
        focus = max(0, focus - 1)
        scroll += 1
    else:
        print("Uh oh… rabbit hole! Time vanishes.")
        focus = max(0, focus - 2)
        scroll += 2
    return focus, scroll

def main():
    # --- VARIABLES (game state) ---
    focus = 2
    scroll = 0
    minutes = 0
    goal_focus = 8 # ERROR 2
    max_minutes = 18
    used_prayer = False
    inventory = ["phone", "notebook"]

    intro()

    # --- LOOP: main loop ---
    while True:
        status(focus, scroll, minutes, inventory)

        # --- CONDITIONS: win/lose checks ---
        if focus >= goal_focus:
            print(wrap("You arrive at youth group alert and joyful. Your mind is clear and ready!"))
            print("🏆 Victory! 'Let your light shine before others.' (Matthew 5:16)")
            break
        if scroll >= 6:
            print(wrap("Brainrot spiral! Too much doomscrolling. You decide to reset and try again."))
            break
        if minutes >= max_minutes:
            print(wrap("Time's up. Youth group is starting. Did you build enough focus?"))
            if focus >= 7:
                print("Nice job—way to keep your mind on good things! 🌟")
            else:
                print("Almost! Next time, try a Scripture/Prayer break earlier.")
            break

        # Player action
        print()
        print("Choose: [W]atch short  [H]ealthy break  [S]cripture/Prayer  [F]riend  [I]nfo  [Q]uit")
        # ERROR 3
        action = input("> ").strip().upper

        minutes += 2  # time passes each turn

        if action == "W":
            focus, scroll = watch_short(focus, scroll)
        elif action == "H":
            focus, scroll, inventory = healthy_break(focus, scroll, inventory)
        elif action == "S":
            focus, used_prayer = scripture_prayer(focus, used_prayer)
        elif action == "F":
            focus, scroll = help_friend(focus, scroll)
        elif action == "I":
            status(focus, scroll, minutes, inventory)
        elif action == "Q":
            print("You put the phone away and head out. See you next time!")
            break
        else:
            print("Try W, H, S, F, I, or Q.")

        # Small chance event each loop
        focus, scroll, inventory = random_event(focus, scroll, inventory)

    print("="*78)
    print("Thanks for playing! Keep your mind on what is lovely and true. (Phil. 4:8)")
    print("="*78)

if __name__ == "__main__":
    main()
