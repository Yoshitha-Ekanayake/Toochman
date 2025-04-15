
class character:
    def __init__ (self, name , health , attack, defense):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.health >= 0

    def take_damage(self, amount):
        damage = max(0, amount - self.defense)
        self.health = self.health - damage

        print (f" {self.name} takes {damage} damage! ( HP: {self.health}/ {self.max_health})")
        return damage


    def heal (self, amount):
        self.health = min(self.max_health, self.health + amount)
        print (f" {self.name} heals for {amount} ( HP: {self.health}/ {self.max_health})")
        

class player(character):

    def __init__ (self, name):
        super().__init__(name, health = 100, attack = 10, defense = 10)
        self.inventory = []
        self.weapon = None
        self.armor = None
        self.blessing =  False
        self.kill_dragon_boost = False
        self.dragon_path = None
        self.stage = 1
        
        
    def equip_weapon(self, weapon):
        self.weapon =weapon
        print (f" {self.name} equips a {weapon.name}! (+ {weapon.damage_boost} ATK)")

    def unequip_weapon(self):
        self.weapon = None
        print (f" {self.name} unequips a {weapon.name}!")

    def equip_armor(self, armor):
        self.armor = armor
        print (f" {self.name} equips a {armor.name}! (+ {armor.defense_boost} DEF)")

    def unequip_armor(self):
        self.armor = None
        print (f" {self.name} unequips a {weapon.name}!")

    def attack_value(self):
        attack_base = self.attack
        if self.weapon:
            attack_base = self.weapon.damage_boost
        if self.kill_dragon_boost:
            attack_base += 15
        return attack_base

    def defense_value(self):
        defense_base = self.defense
        if self.weapon:
            defense_base = self.defense.defense_boost
        if self.kill_dragon_boost:
            defense_base += 15
        return defense_base

    def add_to_inventory(self, item):
        
        self.inventory.append(item)
        print(f" {item.name} added to inventory!")

    def use_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                item.use(self)
                self.inventory.remove(item)
                return
        print("Item not found in inventory")
        
class item:

    def __init__(self, name = str, usage =  str):
        self.name =  name
        self.usage =  usage
        

    def use (self):
        if self.name == "heal_potion":
            player.health +=  min(self.max_health, self.health + 15)

        if self.name == "damage_boost_potion":
            player.attack += 5

class armor:

    def __init__(self, name = str , defense_boost = int , armor_type = str , grade = str ):
        self.name = name
        self.defense_boost = defense_boost
        self.armor_type = armor_type
        self.grade = grade


class weapon:

    def __init__(self, name = str , damage_boost = int , weapon_type = str , grade = str ):
        self.name = name
        self.damage_boost = damage_boost
        self.weapon_type = weapon_type
        self.grade = grade
    
    
class mini_boss (character):

    def __init__(self, name, health, attack, defense, stage):
        super().__init__(name, health, attack, defense)
        self.stage = stage
    



class enemy(character):
    
    def __init__(self, name, health, attack, defense, stage):
        super().__init__(name, health, attack, defense)
        self.stage = stage
  
        
class stage:
    def __init__ (self, number, enemies, mini_boss, boss, side_quests = None):
        self.number = number
        self.enemies = enemies
        self.mini_boss = mini_boss
        self.boss = boss
        self.side_quests = side_quests or []
        self.cleared = False

    def start_stage(self, player):
        print (f"\n >>> Stage {self.number} Begins ! <<<")

        for enemy in self.enemies:
            self.battle_enemy(player,enemy)
            

            if not player.is_alive():
                print("you died! Game over.")
                return

        #print(f"Mini- boss Approaching: {self.mini_boss.name}")
        #self.battle_enemy(player, self.mini_boss)

        '''if player.is_alive():
            #print(f"Boss Encounter: {self.boss_name}")
            #self.batlle_enemy(player, self.boss)'''
            

        if player.is_alive():
            print(f"stage {self.number} cleared!")
            self.cleared =  True
            player.stage += 1
    def make_enemies (self):
        pass
        
    def battle_enemy(self, player, enemy):
        print(f"\nYou Encounter a wild {enemy.name}")

        while player.is_alive() and enemy.is_alive():
            damage = player.attack_value()
            enemy.take_damage(damage)

            if enemy.is_alive():
                player.take_damage(enemy.attack)
                input()
        if not enemy.is_alive():
            print(f"{enemy.name} is defeated!")


    def show_quests(self):
        print(f"\n >> Side Quests in stage {self.number} <<")
        for quest in self.side_quests:
            print(f" ::: {quest} :::")
            
              

wolf = enemy("wolf", 30, 15,2, stage =1)
snake = enemy("snake", 30, 15,3, stage = 1)

stage1 = stage(
    number = 1,
    enemies = [wolf, snake],
    mini_boss = None,
    boss = None,
    side_quests = None )

player = player("Asha")
stage1.start_stage(player)

heal_potion = ("heal_potion", "heals 15 health")
damage_boost_potion("damage_boost_potion", "increase 5 attack")




    
    
            
        
