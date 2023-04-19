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
        self.code = False
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
        self.current_room = "Generator Room"
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
    x = input("Search Options: top, middle, or bottom shelf?: ").lower()
    time.sleep(1)
    if x == "bottom":
        if p.caplog == True:
            print("\nAs you look again, you notice a small piece of paper near the shelf that you didn't see before.\n")
            time.sleep(3)
            print("On the paper is written: 85290184\n")
            time.sleep(2)
            print("Great, you've found the code!\n")
            time.sleep(2)
            print("The Captain's Log said they were in the Master Chamber! We better hurry...\n")
            p.code = True
            time.sleep(3)
            print("As you turn to leave, you hear noises coming from the living quarters nearby.\n")
            time.sleep(4)

            pass
        elif p.caplog == False:
            p.fuse = True
            print("\nYou found the Fuse!\n")
        
    elif x == "middle":
        print("\nSome find screws and a box of trash bags, but nothing useful here.\n")
        Fuse()
    elif x == "top":
        print("\nYou found nothing but a dusty shelf\n")
        Fuse()
    else:
        print("\nInvalid input, please enter top, middle, or bottom.\n")
        Fuse()
    pass

#Init player as p
p = player()
spaceship = Spaceship()
def intro():
    p.name = input("What is your character's name? ")
    print('\n', "Welcome to the game" , p.name , '\n')
    print(spaceship.rooms[spaceship.current_room].description)
    time.sleep(2)
    print("\nYou wake up…. You're confused, the sounds of sirens fill your ears. It is dark with only the emergency lights dimly shining.\n")
    time.sleep(2)
    print("You get up and yell for help to no avail, it seems like you're the only one left on this ship.\n")
    print("--------------------------------------")
    while True:
        if spaceship.current_room == "Flight Deck":
            #if p.weapon == False:
            #if p.weapon == True:
            pass

        if spaceship.current_room == "Cafeteria":
            if p.caplog ==True:
                pass
            elif p.lights == True:
                p.caplog = True
                time.sleep(1)
                print("\nAs you enter the Cafeteria, assisted by the newly brightened room, you discover a book laying on the table.")
                time.sleep(1)
                print('\nYou pick up the book, reading the words written on the cover "Captains Log"\n')
                time.sleep(2)
                print("As you open the Captains log, there are many pages of general notes, maintenance slips, and other seemingly normal entries.\n")
                time.sleep(3)
                print("You reach a slightly crumbled page in the book and notice the last entry was only 72 hours ago… it reads,\n")
                time.sleep(4)
                print('"This is where my log ends", \n\n"It seems that all hope is lost", \n\n"Our only hope is that the mothership received our SOS signal but it seems like our luck has run out"\n')
                time.sleep(3)
                print('"If anyone is reading this watch out for geashes they are extremely intelligent!"\n')
                time.sleep(6)
                print("Geashes? What is that?...\n")
                time.sleep(5)
                print("You continue to read...\n")
                time.sleep(3)
                print('"...after a geashes destroyed the terminal,\nI had to store our weapons in the master chamber with the rest of the crew to prevent it from destroying them"\n')
                time.sleep(4)
                print('"if anyone from the outside is reading this PLEASE SAVE US! YOURE NOT ALONE!"\n')
                time.sleep(4)
                print('“The code to save us can be found in the storage closet, please move with haste as we wont have much time!”\n')
            pass
    
        if spaceship.current_room == "Living Quarters":
            if p.code == True:
                time.sleep(3)
                print("GEASHES!!\n")
            pass
    
        if spaceship.current_room == "Master Chamber":
            #if p.lights == True:
            #if p.lights == False:
                #pass
            pass
    
        if spaceship.current_room == "Generator Room":
            if p.lights ==True:
                pass
            elif p.fuse == False:
                time.sleep(3)
                print("\nYou look around and in the dim light, you notice something on the wall.\n")
                time.sleep(2)
                print("It's the fuse panel, you determine, but there is a broken fuse.\n")
                time.sleep(2)
                print("Luckily you remember there are extras in the storage room.\n")
                pass
            elif p.fuse == True:
                p.lights = True
                print("\nAs you walk into the generator room you find the fuse panel and place the fuse you found inside the slot.\n")
                time.sleep(2)
                print("You fumble around and find the main power switch. With a bit of effort, you are able to flip the switch.\n")
                time.sleep(2)
                print("You get the power back on and instantly the dimly lit ship is bright with the light of LED lights shining.\n")
                time.sleep(2)
                print("It may be a good time to get familiar with the ship.\n")
                pass
            pass
    
        if spaceship.current_room == "Storage":
            if p.fuse == False:
                time.sleep(1)
                print("\nThere is a shelf in here with various items on it. \n")
                time.sleep(1)
                print("You decide to search the shelves.\n")
                Fuse()
            if p.caplog == True:
                print("\nYou could have sworn you checked all the shelves...\n")
                Fuse()

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




        

      




