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
        if self.health <= damage:
            print(f"{self.name} died. Please try again!")
        else:
            print(f"{self.name} has {self.health} remaining")


# player.take_damage(9)
# player.take_damage(81)
# class new(playerCharacter):
#     def __init__(self, inventory):
#         playerCharacter.__init__(self)
#         self.inventory = "Weapon"
        
p = player()
p.name = input("What is your character's name? ")
print("Welcome" , p.name)
p.weapon = False
if p.weapon == True:
    print("You have a weapon!")
    p.attack_damage = 10
if p.weapon == False:
    print("You are defenseless!")
    p.attack_damage = 0