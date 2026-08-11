import random

class Blossom:
    def __init__(self):
        print("Welcome to Blossom!")
        self.name = input("Enter your character's name: ")
        self.health = 10
        self.hunger = 5
        self.thirst = 5
        self.inventory = ["Knife"]
        self.day = 1
        self.alive = True
        print("\n{}, the world has fallen. Survive as long as you can!\n".format(self.name))

    def start(self):
        while self.alive:
            print(f"\n--- Day {self.day} ---")
            self.status()
            self.choose_action()
            self.random_event()
            self.day += 1

    def status(self):
        print(f"Health: {self.health} | Hunger: {self.hunger} | Thirst: {self.thirst}")
        print(f"Inventory: {self.inventory}")

    def choose_action(self):
        print("\nChoose your action for the day:")
        print("1 - Search for Food")
        print("2 - Search for Water")
        print("3 - Explore Ruins")
        print("4 - Rest")
        choice = input("Enter 1-4: ")

        if choice == "1":
            self.search_food()
        elif choice == "2":
            self.search_water()
        elif choice == "3":
            self.explore()
        elif choice == "4":
            self.rest()
        else:
            print("Invalid choice! You waste time...")
            self.hunger += 1
            self.thirst += 1
        self.check_alive()

    def search_food(self):
        print("\nYou search the area for food...")
        found = random.choice(["Canned Food", "Nothing", "Infected Meat"])
        if found == "Nothing":
            print("You found nothing.")
            self.hunger += 1
        elif found == "Infected Meat":
            print("You accidentally eat infected meat! 🤢")
            self.health -= 3
            self.hunger = max(self.hunger - 2, 0)
        else:
            print(f"You found {found}!")
            self.inventory.append(found)
            self.hunger = max(self.hunger - 3, 0)

    def search_water(self):
        print("\nYou search for water...")
        found = random.choice(["Clean Water", "Nothing", "Contaminated Water"])
        if found == "Nothing":
            print("You found nothing.")
            self.thirst += 1
        elif found == "Contaminated Water":
            print("You drank contaminated water! 🤢")
            self.health -= 2
            self.thirst = max(self.thirst - 2, 0)
        else:
            print(f"You found {found}!")
            self.inventory.append(found)
            self.thirst = max(self.thirst - 3, 0)

    def explore(self):
        print("\nYou explore abandoned ruins...")
        encounter = random.choice(["Infected Human", "Safe", "Abandoned Supplies", "Trap"])
        if encounter == "Infected Human":
            print("An infected human attacks! ⚔️")
            if "Knife" in self.inventory:
                print("You fight it off with your Knife!")
                self.inventory.remove("Knife")
                print("Your Knife broke.")
            else:
                self.health -= 3
        elif encounter == "Safe":
            print("The ruins are empty. You find nothing but shadows.")
        elif encounter == "Abandoned Supplies":
            supply = random.choice(["Medkit", "Canned Food", "Water Bottle"])
            print(f"You found {supply}!")
            self.inventory.append(supply)
        else:
            print("You triggered a trap! You take damage.")
            self.health -= 2
        self.hunger += 1
        self.thirst += 1

    def rest(self):
        print("\nYou take a rest to regain health...")
        self.health = min(self.health + 2, 10)
        self.hunger += 1
        self.thirst += 1

    def random_event(self):
        print("\nRandom event of the day...")
        event = random.choice(["Nothing", "Zombie Ambush", "Friendly Survivor", "Weather"])
        if event == "Nothing":
            print("A quiet day... nothing happens.")
        elif event == "Zombie Ambush":
            print("A zombie ambush! You barely escape.")
            if "Knife" in self.inventory:
                print("You fend them off with your Knife. Knife breaks.")
                self.inventory.remove("Knife")
            else:
                self.health -= 3
        elif event == "Friendly Survivor":
            print("You meet a friendly survivor who gives you a Medkit!")
            self.inventory.append("Medkit")
        else:
            print("Harsh weather today! Hunger and thirst increase.")
            self.hunger += 1
            self.thirst += 1
        self.check_alive()

    def check_alive(self):
        if self.health <= 0:
            self.alive = False
            print("\nYour health dropped to zero. You have died. Game Over 😵")
            exit()
        if self.hunger >= 10:
            self.alive = False
            print("\nYou starved to death. Game Over 😵")
            exit()
        if self.thirst >= 10:
            self.alive = False
            print("\nYou died of dehydration. Game Over 😵")
            exit()

# Start the game
game = Blossom()
game.start()