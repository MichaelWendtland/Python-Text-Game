class playerCharacter:
    def __init__(self, name, health, health_max):
        self.name = name
        self.health = health
        self.health_max = health_max
        #self.inventory = inventory
        
    def attack(self):
        print(f"The {self.name} attacks for {self.attack_damage} damage")
        
    def take_damage(self, damage):
        self.health -=damage
        if self.health <= damage:
            print(f"{self.name} died. Please try again!")
        else:
            print(f"{self.name} has {self.health} remaining")

# player = playerCharacter("Bob", 100, 100)
# player.take_damage(9)
# player.take_damage(81)