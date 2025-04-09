from weapons import fists


class Character:

    def __init__(self, name , health):

        self.name = name
        self.health = health
        self.health_max = health

        self.weapon = fists
        
    def attack (self, target):
        
        target.health -= self.weapon.damage # weapon class eke damage kiyana eka call karanawa
        target.health = max(target.health , 0)
        print(f"damage dealt by {self.name} with {self.weapon.name} to {target.name} is {self.weapon.damage}")
        

class hero(Character):

    def __init__ (self, name , health):

        super().__init__(name = name, health =  health)

        self.default_weapon = self.weapon

    def equip (self, weapon):
        
        self.weapon = weapon
        print(f"{self.name} equipped a {self.weapon.name}!")

    def drop(self):
        
        print(f"{self.name} dropped {self.weapon.name}!")
        self.weapon = self.default_weapon
        #print((f"{self.name} dropped {self.weapon}!")


class enemy(Character):

    def __init__ (self, name , health, weapon):

        super().__init__(name = name, health =  health)
        self.weapon = weapon
