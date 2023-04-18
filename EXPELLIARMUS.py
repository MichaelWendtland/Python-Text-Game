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
            
            if p.wire == False:
                pass
            if p.wire == True:
                pass
            pass
    
        if spaceship.current_room == "Storage":
            if p.caplog == True and p.weapon == False:
                x = input("Search Options: top, middle, or bottom shelf?: ")
                if x == "bottom":
                    p.weapon = True
                    print("You have acquired the HiMagNetic7000!")
                if x == "middle":
                    print("Some find screws and a box of trash bags, but nothing useful here.")
                if x == "top":
                    print("You found nothing but a dusty shelf")
                if None:
                    print("Invalid input, please enter top, middle, or bottom.")
                pass   

        print(spaceship.available_directions())
        direction = input("Enter direction or 'exit' to quit: ").lower()

        if direction == "exit":
            go()
            break
        spaceship.navigate(direction)

