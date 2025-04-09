from weapons import weapon


class armour:

    def __init__(self, name,armour_type, damage_reduction):
        self.name = name
        self.armour_type = armour_type
        self.damage_reduction = damage_reduction
        self.weapon.damage = damage
        

plain_armour = armour(name = "plain_armour", armour_type = "plain", damage_reduction = damage*0.1) 
bronze_armour = armour(name = "bronze_armour", armour_type = "bronze", damage_reduction = damage*0.2) 
silver_armour = armour(name = "silver_armour", armour_type = "silver", damage_reduction = damage*0.3) 
        
