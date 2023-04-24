print("""
Find the Dragon Egg
===================

Your quest starts.
""")

rooms = ["hometown", "beekeeper", "forest", "clearing"] # list rooms that are in your game

descriptions = {
    "hometown": "You are in your home town...",
    "beekeeper": "You hear bees and smell the scent of sweet honey...",
    "forest": "Fresh air fills your lungs, the smell of wood is in the air and you hear the birds singing...",
    "clearing": "Sun shines into your eyes and you feel your skin getting warm..."
}

paths = {
    "hometown": ["beekeeper", "forest"],
    "forest": ["clearing", "beekeeper"],
    "beekeeper": ["forest", "hometown"],
    "clearing": ["forest", "beekeeper"]
}

room = "hometown"
honey = False
bear = False

print("After accepting the Quest, you find yourself in your room in your hometown. You find a letter on your bed, with a hint that you have to visit a beekeeper at a forest near you...")

while room != "clearing":
    target = input(f"Where would you like to go?: {rooms}: ").lower()
    if target in paths[room]:
        print(descriptions[target])
        room = target
        if room == "beekeeper" and not honey:
            print("The beekeeper gives you a jar of honey. Yum!")
            honey = True
        elif room == "beekeeper" and honey:
            print("The beekeeper thanks you for your visit, but you already have honey.")
        elif room == "forest":
            if honey:
                print("You leave the honeypot for the bear and carefully sneak by.")
                honey = False
                bear = True  
            else:
                print("There is a BEAR in the forest!!! You run away.")
                room = "hometown"
    else:
        print("You cant reach the location from here!")
    print(f"You are in {room}")

else:
    if bear:
        print("""
        On a hidden clearing you discover the dragon egg.
        Your quest has been successful!
        """)
        input("Random key for ending the game...")
    