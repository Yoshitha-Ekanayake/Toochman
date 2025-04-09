class weapon:
    
    def __init__(self, name , weapon_type, damage, value):
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value


iron_sword = weapon(name = "iron_sword" , weapon_type = "slash" , damage = 5, value = 10)
short_bow = weapon(name = "short bow" , weapon_type = "pierce" , damage = 8, value = 8)
fists = weapon(name = "fists" , weapon_type = "blunt" , damage = 3, value = 4)


        
        
