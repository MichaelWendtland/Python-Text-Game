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
        self.rooms["Master Chamber"].doors["East"] = "Cafeteria"
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

# Test the Spaceship class
spaceship = Spaceship()
print(spaceship.rooms[spaceship.current_room].description)
while True:
    print(spaceship.available_directions())
    direction = input("Enter direction or 'exit' to quit: ").lower()
    if direction == "exit":
        break
    spaceship.navigate(direction)
