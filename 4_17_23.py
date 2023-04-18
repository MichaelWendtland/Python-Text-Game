#import time module
import time
from PlayerClass import playerCharacter
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
class Spaceship:
    def __init__(self):
        self.current_room = "Generator Room"
        self.rooms = {
            "Flight Deck": Room("Flight Deck", "You are on the flight deck."),
            "Generator Room": Room("Generator Room", "You are in the generator room."),
            "Storage": Room("Storage", "You are in the storage room."),
            "Cafeteria": Room("Cafeteria", "You are in the cafeteria."),
            "Master Chamber": Room("Master Chamber", "You have entered the master chamber"),
            "Living Quarters": Room("Living Quarters","You are in the Living Quarters This is where you and your crew slept.")
        }
        self.rooms["Flight Deck"].doors["south"] = "Cafeteria"
        self.rooms["Cafeteria"].doors["south"] = "Living Quarters"
        self.rooms["Cafeteria"].doors["west"] = "Master Chamber"
        self.rooms["Cafeteria"].doors["north"] = "Flight Deck"
        self.rooms["Living Quarters"].doors["east"] = "Storage"
        self.rooms["Living Quarters"].doors["north"] = "Cafeteria"
        self.rooms["Living Quarters"].doors["south"] = "Generator Room"
        self.rooms["Master Chamber"].doors["east"] = "Cafeteria"
        self.rooms["Generator Room"].doors["north"] = "Living Quarters"
        self.rooms["Storage"].doors["west"] = "Living Quarters"

    def navigate(self, direction):
        next_room = self.rooms[self.current_room].doors.get(direction)
        if next_room is None:
            print("You cannot go that way.")
        else:
            self.current_room = next_room
            print(self.rooms[self.current_room].description)

    def available_directions(self):
        directions = [direction for direction, room in self.rooms[self.current_room].doors.items() if room is not None]
        return f"You can go: {', '.join(directions)}"
he
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.doors = {"north": None, "south": None, "east": None, "west": None}

p = player()
directions = 'This line will show directions'
def intro():
    p.name = input("What is your character's name? ")
    print('\n', "Welcome to the game" , p.name , '\n')
    print(line[5], '\n')
    time.sleep(4)
    print(line[8])
    time.sleep(4)
    spaceship = Spaceship()
    print(spaceship.rooms[spaceship.current_room].description)
    while True:
        if spaceship.current_room == "Flight Deck":
            pass

        if spaceship.current_room == "Cafeteria":
            def cafeteria_room():
                print("You enter the cafeteria and see a captain's log on the table.")
                player.add_to_inventory("captain's log")
    
        if spaceship.current_room == "Living Quarters":
            time.sleep(3)
            print("You look around and see that there are no crew mates in here, however you have the feeling that your being watched")
    
        if spaceship.current_room == "Master Chamber":
            pass
    
        if spaceship.current_room == "Generator Room":
            time.sleep(3)
            print("you walk over to the generator and see that the main power switch was flipped off, you flip the switch to the on position and suddenly the lights turn on and you decied to look for your crew mates")
    
        if spaceship.current_room == "Storage":
            time.sleep(3)
            print("you walk into the storage room and see boxes of material, you dont need any of this right now however.")
    
        print(spaceship.available_directions())
        direction = input("Enter direction or 'exit' to quit: ").lower()

        if direction == "exit":
            break
        spaceship.navigate(direction)


        


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




        

      





