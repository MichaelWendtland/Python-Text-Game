#import time module
import time
#Open storyline files and init function line to read the story
with open('story.txt','r', encoding = "utf8") as s:
    a = s.readlines()
    i = 1
    line = {}
    for x in a:
        x = x.rstrip('\n')
        x = x.rstrip('')
        line[i] = x
        i += 1

def go():
    print(" _____   ___  ___  ___ _____   _____  _   _ ___________ \n"
            "|  __ \ / _ \ |  \/  ||  ___| |  _  || | | |  ___| ___ \ \n"
            "| |  \// /_\ \| .  . || |__   | | | || | | | |__ | |_/ /\n"
            "| | __ |  _  || |\/| ||  __|  | | | || | | |  __||    / \n"
            "| |_\ \| | | || |  | || |___  \ \_/ /\ \_/ / |___| |\ \ \n"
            " \____/\_| |_/\_|  |_/\____/   \___/  \___/\____/\_| \_|\n")
#Init player spawn with no name, 100 health/100, empty inventory, no weapon
class player:
    def __init__(self):
        self.name = ""
        self.health = 100
        self.health_max = 100
        self.attack_damage = 0
        self.inventory = ""
        self.weapon = False
        
    def attack(self):
        print(f"The {self.name} attacks for {self.attack_damage} damage")
        
    def take_damage(self, damage):
        self.health -=damage
        if self.health <= 0:
            print(f"{self.name} died. Please try again!", '\n')
            go()
        else:
            print(f"{self.name} has {self.health} remaining")
            
class geashesMonster:
    def __init__(self, name, health, attack_damage):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage
        
    def attack(self):
        print(f"The {self.name} attacks for {self.attack_damage} damage!")
        
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"The {self.name} has {self.health} health remaining.")

#this is the monster, it has a health of 20 and a attack dammage of 10
#geashes = geashesMonster ("Geashes", 20, 10)
#use .attack to call on the monster to attack
#geashes.attack()
# #this line is for telling how much dammage was given by the player, use this as an example
# geashes.take_damage(19)
# geashes.take_damage(1)

#Init player as p
p = player()
directions = 'This line will show directions'
def intro():
    p.name = input("What is your character's name? ")
    print('\n', "Welcome to the game" , p.name , '\n')
    time.sleep(2)
    print(line[5], '\n')
    time.sleep(5)
    print(line[8], '\n')
    time.sleep(1)
    print(directions)


#Main Menu
def main_menu():
    print("Welcome to the Game Menu!")
    print("1. Start Game")
    print("2. Load Game")
    print("3. Quit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        start_game()
    elif choice == "2":
        load_game()
    elif choice == "3":
        quit_game()
    else:
        print("Invalid choice. Please try again.")
        main_menu()
   
def start_game():
    print("Starting new game...")
    print("Game started!")
    intro()
    #main_menu()

def load_game():
    print("Loading game...")
    # Add your code for loading a game here
    print("Game loaded!")
    main_menu()

def quit_game():
    print("Exiting game...")
    exit()

if __name__ == '__main__':
    main_menu()




        

      





