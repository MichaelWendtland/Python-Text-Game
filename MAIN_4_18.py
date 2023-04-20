#import time module
import time
#Open storyline files and init function line to read the story
#with open('story.txt','r', encoding = "utf8") as s:
#    a = s.readlines()
#    i = 1
#    line = {}
#    for x in a:
#        x = x.rstrip('\n')
#        x = x.rstrip('')
#        line[i] = x
#        i += 1
    
#This function is to print game over
def go():
    print(" _____   ___  ___  ___ _____   _____  _   _ ___________ \n"
            "|  __ \ / _ \ |  \/  ||  ___| |  _  || | | |  ___| ___ \ \n"
            "| |  \// /_\ \| .  . || |__   | | | || | | | |__ | |_/ /\n"
            "| | __ |  _  || |\/| ||  __|  | | | || | | |  __||    / \n"
            "| |_\ \| | | || |  | || |___  \ \_/ /\ \_/ / |___| |\ \ \n"
            " \____/\_| |_/\_|  |_/\____/   \___/  \___/\____/\_| \_|\n")
#Init player spawn with no name, 100 health/100, empty inventory, no weapon, all items=false
class player:
    def __init__(self):
        self.name = ""
        self.health = 100
        self.health_max = 100
        self.attack_damage = 10
        self.cpu = False
        self.weapon = False
        self.caplog = False
        self.fuse = False
        self.lights = False
        self.code = False
        self.scare = False
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

#The class for geashesMonster establishes name, health, attack damage; as well as attack and take_damage       
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
       # geashes = geashesMonster ("Geashes", 20, 10)
#use .attack to call on the monster to attack
       # geashes.attack()
# #this line is for telling how much dammage was given by the player, use this as an example
        #geashes.take_damage(19)
        #geashes.take_damage(1)

#Spaceship class-Identifies each room and provides a description of each room to be read to the player upon entry
class Spaceship:
    def __init__(self):
        self.current_room = "Generator Room"
        self.rooms = {
            "Flight Deck": Room("Flight Deck", "\nYou are on the flight deck.\n"),
            "Generator Room": Room("Generator Room", "\nYou are in the generator room.\n"),
            "Storage": Room("Storage", "\nYou are in the storage room.\n"),
            "Cafeteria": Room("Cafeteria", "\nYou are in the cafeteria.\n"),
            "Master Chamber": Room("Master Chamber", "\nYou have entered the master chamber.\n"),
            "Living Quarters": Room("Living Quarters","\nThis is where you and your crew slept.\n")
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

#This is the class for room
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.doors = {"north": None, "south": None, "east": None, "west": None}

#This function is the simple shelf program to search for the fuse and the code
def Fuse():
    x = input("Search Options: top, middle, or bottom shelf?: ").lower()
    time.sleep(1)
    if x == "bottom":
        if p.weapon == True:
            time.sleep(2)
            print("There's nothing left on the bottom shelf.")
            Fuse()
            pass
        elif p.caplog == True:
            print("\nAs you look again, you notice a small piece of paper near the shelf that you didn't see before.\n")
            time.sleep(3)
            print("On the paper is written: 85290184\n")
            time.sleep(2)
            print("Great, you've found the code!\n")
            time.sleep(2)
            print("The Captain's Log said they were in the Master Chamber! We better hurry...\n")
            p.code = True
            p.scare = True
            time.sleep(3)
            print("As you turn to leave, you hear noises coming from the living quarters nearby. Maybe a crew member?\n")
            time.sleep(4)
            pass
        elif p.caplog == False:
            p.fuse = True
            print("\nYou found the Fuse!\n")
        
    elif x == "middle":
        print("\nSome find screws and a box of trash bags, but nothing useful here.\n")
        Fuse()
    elif x == "top":
        if p.weapon == True:
            print("\n You have found the CPU!\n ")
            p.cpu = True
            pass
        elif p.weapon == False:
            print("\nYou found nothing but a dusty shelf, and some sort of computer part.\n")
            Fuse()
    else:
        print("\nInvalid input, please enter top, middle, or bottom.\n")
        Fuse()
    pass

#Init class player as p
p = player()

#Init Class Spaceship as spaceship
spaceship = Spaceship()

#Main driver code:
def driver():
    #establish p.name with player name input
    p.name = input("What is your character's name? ")
    #welcome player to game, show starting room name, begin intro dialog
    print('\n', "Welcome to the game" , p.name , '\n')
    print(spaceship.rooms[spaceship.current_room].description)
    time.sleep(2)
    print("\nYou wake up…. You're confused, the sounds of sirens fill your ears. It is dark with only the emergency lights dimly shining.\n")
    time.sleep(2)
    print("You get up and yell for help to no avail, it seems like you're the only one left on this ship.\n")
    print("--------------------------------------")
    #Establish the map and starting pos
    while True:
        #Locate the room, and depending on the p.*args: play coresponding dialog/functions
        if spaceship.current_room == "Flight Deck":
            #if p.weapon == False:
            if p.cpu == True:
                print("\nFLIGHT CONTROLS NOW ACTIVE\n")
                time.sleep(2)
                print("THIS THE MOTHERSHIP, WE ARE COMING IN HOT BABY! \n\n WATCH UR TAIL! THE GEASHES ARE MEANY HEADS\n")
            pass

        if spaceship.current_room == "Cafeteria":
            if p.weapon == True:
                geashes = geashesMonster ("Geashes", 10, 10)
                print("Geashes appears infront of you!")
                print("options: Use HiMagNetic7000")
                userinput = input("Type HiMagNetic7000")
                if userinput == "HiMagNetic7000":
                    print("You use your HiMagNetic7000 and deal 10 dammage")
                    geashes.take_damage(10)

            #if captains log has been read, skip reading the log text again
            elif p.caplog ==True:
                pass

            #if the lights have been turned on, Player receives captains log, play captains log text
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
                print('"If anyone from the outside is reading this PLEASE SAVE US! YOURE NOT ALONE!"\n')
                time.sleep(4)
                print('“The code to save us can be found in the storage closet, please move with haste as we wont have much time!”\n')
            pass

        #This is where the player first encounters the Geashes after receiving the code
        if spaceship.current_room == "Living Quarters":
            if p.scare == True:
                time.sleep(3)
                print("\nAs you enter the Living Quarters, you realise that wasn't a crewmate, but rather the geashes that the captain warned about!\n")
                time.sleep(2)
                print("The geashes staggers back and climbs up the wall and into the open vent in the ceiling.\n")
                p.scare = False

            pass

        #This is where the player enters the code and receives the HiMagNetic7000
        if spaceship.current_room == "Master Chamber":
            if p.weapon ==True:
                pass
            elif p.code == True:
                time.sleep(2)
                print("\nYou finally have made it to the master chamber, you look at the crumpled up note with the 8 digit code on it.\n")
                time.sleep(2)
                print("The numbers on the paper read: 85290184\n")
                time.sleep(2)
                print("You type the code into the door security panel, 8-5-2-9-0-1-8-4.\n")
                time.sleep(2)
                print("The screen reads out --ACCESS DENIED--.\n")
                time.sleep(2)
                print("You decide to try again, but backwards 4-8-1-0-9-2-5-8.\n\n This time the panel reads --ACCESS GRANTED-- and you hear a door latch open.\n")
                time.sleep(3)
                print("You open the door. To your horror, the entire 6 man crew is not there... the only thing left of them is their bones…\n")
                time.sleep(2)
                print("As you look around the room, you discover another note.\n")
                time.sleep(2)
                print('It reads, "This is my final message,"\n\n "The Geashes has breached containment and the onlything that can prevent it from killing all of us is if we use the HiMagNetic7000." \n\n "Its the only weapon that geashes is vulnerable to and unfortunately mine has ran out of power since geashes has destroyed the generator"')
                time.sleep(4)
                print("You look back to where you found the note to see a gun shaped object that is glowing with a light blue aurora on its side.\n")
                time.sleep(3)
                print("It reads, “HiMagNetic7000”, it seems that turning on the generator has made the weapon function again.\n\n You pick it up and carry it with you. You think to yourself that this HiMagNetic7000 will be very useful.\n")
                time.sleep(4)
                print('As you turn to leave the master chamber, you think to yourself:\n\n "Now is the best time to get back to the flight deck to get in contact with the mothership"\n')
                p.weapon = True
            elif p.weapon == True:
                pass
            pass

        #This is where the player starts the game and where the fuse will be returned to
        if spaceship.current_room == "Generator Room":
            if p.lights ==True:
                pass
            #Read if the player has not acquired the fuse
            elif p.fuse == False:
                time.sleep(3)
                print("\nYou look around and in the dim light, you notice something on the wall.\n")
                time.sleep(2)
                print("It's the fuse panel, you determine, but there is a broken fuse.\n")
                time.sleep(2)
                print("Luckily you remember there are extras in the storage room.\n")
                pass
            #Read if the player has found the fuse
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

        #This is where the player finds the fuse and the code (Includes simple shelf search function Fuse())
        if spaceship.current_room == "Storage":
            #If the code has already been found skip dialog
            if p.weapon == True:
                Fuse()
            elif p.code == True:
                pass
            #If the player has not found the fuse, start Fuse() to search shelves (dialog = fuse)
            elif p.fuse == False:
                time.sleep(1)
                print("\nThere are shelves in here that contain various items. \n")
                time.sleep(1)
                print("You decide to search the shelves.\n")
                Fuse()
            #If the player has found the captains log, start Fuse() to search for the code
            elif p.caplog == True:
                print("\nYou could have sworn you checked all the shelves...\n")
                Fuse()

            pass
        #Print the available movement after the player has received any dialog/items
        print(spaceship.available_directions())
        direction = input("Enter direction or 'exit' to quit: ").lower()
        #If the player would like to quit at any time:
        if direction == "exit":
            #Play the "GAME OVER" large print
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
    driver()
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




        

      





