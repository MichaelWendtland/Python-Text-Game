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
        self.caplog = False
        self.fuse = False
        self.lights = False
    def inventory(self):
        pass
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


class Spaceship:
    def __init__(self):
        self.current_room = "Flight Deck"
        self.rooms = {
            "Flight Deck": Room("Flight Deck", "You are on the flight deck."),
            "Generator Room": Room("Generator Room", "You are in the generator room."),
            "Storage": Room("Storage", "You are in the storage room."),
            "Cafeteria": Room("Cafeteria", "You are in the cafeteria."),
            "Master Chamber": Room("Master Chamber", "You have entered the master chamber"),
            "Living Quarters": Room("Living Quarters","This is where you and your crew slept.")
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

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.doors = {"north": None, "south": None, "east": None, "west": None}
        
def Fuse():
    if p.caplog == True:
        x = input("Search Options: top, middle, or bottom shelf?: ")
        if x == "bottom":
            p.fuse = True
            print("You have acquired the Fuse")
            p.lights = True
            pass
        if x == "middle":
            print("Some find screws and a box of trash bags, but nothing useful here.")
            Fuse()
        if x == "top":
            print("You found nothing but a dusty shelf")
            Fuse()
        if None:
            print("Invalid input, please enter top, middle, or bottom.")
            Fuse()
        pass
#Init player as p
p = player()
spaceship = Spaceship()
def intro():
    p.name = input("What is your character's name? ")
    print('\n', "Welcome to the game" , p.name , '\n')
    p.weapon = False
    if p.weapon == True:
        print("You have a weapon!")
        p.attack_damage = 10
    if p.weapon == False:
        print("You are defenseless!")
        p.attack_damage = 0
    print(spaceship.rooms[spaceship.current_room].description)
    while True:
        if spaceship.current_room == "Flight Deck":
            #if p.weapon == False:
            #if p.weapon == True:
            pass

        if spaceship.current_room == "Cafeteria":
            #if p.weapon == False:
                #pass
            #if p.weapon == True:
            
            pass
    
        if spaceship.current_room == "Living Quarters":
            #weapons, lights, caplog = true spawn:
            #spawn first geashes
            pass
    
        if spaceship.current_room == "Master Chamber":
            #if spaceship lights = true
            #if spaceship lights = false
            pass
    
        if spaceship.current_room == "Generator Room":
            
            if p.fuse == False:
                p.caplog = True
                print("You have found the captain's log")
                pass
            if p.fuse == True:
                print("As you walk into the generator room you find the Fuse panel and place the fuse you found inside the slot.\n")
                print("You flip the switch to the on position and suddenly the lights turn on and you decied to look for your crew mates")
                p.lights = True
                pass
            pass
    
        if spaceship.current_room == "Storage":
            if p.caplog == True and p.fuse == False:
                Fuse()
            if p.caplog == False:
                pass
            pass

        print(spaceship.available_directions())
        direction = input("Enter direction or 'exit' to quit: ").lower()

        if direction == "exit":
            go()
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




        

      





