
class character:
    def __init__ (self, name , health , attack, defense):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.health >= 0

    def take_damage(self, damage_handler, weapon_type=None, attacker=None):
        damage = damage_handler.calculate_damage(
            target=self,
            weapon_type=weapon_type,
            attacker=attacker)
        self.health -= damage
        print(f"{self.name} takes {damage} damage! (HP: {self.health}/{self.max_health})")

        # Apply special effects from attacker’s weapon
        if damage_handler.special_effect:
            damage_handler.apply_effect(self, damage_handler.special_effect)

        return damage

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
        print (f" {self.name} equips a {self.weapon.name}! (+ {self.weapon.damage_boost} ATK)")

    def unequip_weapon(self):
        print (f" {self.name} unequips a {self.weapon.name}!")
        self.weapon = None
        

    def equip_armor(self):
        self.armor = armor
        print (f" {self.name} equips a {armor.name}! (+ {armor.defense_boost} DEF)")

    def unequip_armor(self):
        print (f" {self.name} unequips a {self.armor.name}!")
        self.armor = None
        

    def attack_value(self):
        attack_base = self.attack
        if self.weapon:
            attack_base += self.weapon.damage_boost
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


class damage_effects:
    
    def init(self, base_damage, weapon_type=None, special_effect=None):
        self.base_damage = base_damage
        self.weapon_type = weapon_type
        self.special_effect = special_effect  # e.g., 'poison', 'burn'

    def calculate_damage(self, target, weapon_type=None, attacker=None):
        damage = self.base_damage

        # Weapon type effectiveness (customize per enemy later)
        if hasattr(target, "weaknesses") and weapon_type in target.weaknesses:
            print(f"{target.name} is weak to {weapon_type}!")
            damage *= 1.5  # 50% bonus damage

        # Defense reduction
        damage = max(0, damage - target.defense)
        return int(damage)

    def apply_effect(self, target, effect):
        if effect == "poison":
            target.status_effects.append({"type": "poison", "damage": 5, "duration": 3})
            print(f"{target.name} is poisoned!")
        elif effect == "burn":
            target.status_effects.append({"type": "burn", "damage": 7, "duration": 2})
            print(f"{target.name} is burned!")
































class armor:

    def __init__(self, name = str , defense_boost = int , armor_type = str , grade = str, special_effect = None):
        self.name = name
        self.defense_boost = defense_boost
        self.armor_type = armor_type
        self.grade = grade
        self.special_effect = special_effect



class bronze_armor(armor):

     def __init__ (self):
        super().__init__ (name = "bornze armor" , defense_boost = 10 , armor_type = "bronze" , grade = "D", special_effect = None)


class silver_armor(armor):

     def __init__ (self):
        super().__init__ (name = "bornze armor" , defense_boost = 15 , armor_type = "silver" , grade = "C", special_effect = "lighting resistance")


class Mythic_armor(armor):

     def __init__ (self):
        super().__init__ (name = "bornze armor" , defense_boost = 25 , armor_type = "platinum" , grade = "B", special_effect = "poison Resistance")


class Lunar_armor(armor):

     def __init__ (self):
        super().__init__ (name = "bornze armor" , defense_boost = 35 , armor_type = "crimson" , grade = "A", special_effect = "Dark magic resistance")



class Phanthom_armor(armor):

     def __init__ (self):
        super().__init__ (name = "bornze armor" , defense_boost = 50 , armor_type = "hellfire" , grade = "S", special_effect = "fiire damage reduction")




class weapon:

    def __init__(self, name = str , damage_boost = int , weapon_type = str , grade = str, special_effect = None ):
        self.name = name
        self.damage_boost = damage_boost
        self.weapon_type = weapon_type
        self.grade = grade


class axe(weapon):

    def __init__ (self):
        super().__init__ (name = "axe" , damage_boost = 10 , weapon_type = "axe", grade = "D", special_effect = None)



class bronze_sword(weapon):

    def __init__ (self):
        super().__init__ (name = "platinum bow" , damage_boost = 10 , weapon_type = "sword", grade = "D", special_effect = None)


class bronze_bow(weapon):

    def __init__ (self):
        super().__init__ (name = "platinum bow" , damage_boost = 15 , weapon_type = "bow", grade = "D", special_effect = None)


class bronze_knife(weapon):

    def __init__ (self):
        super().__init__ (name = "platinum bow" , damage_boost = 9 , weapon_type = "knife", grade = "D", special_effect = None)

        
class silver_sword(weapon):

    def __init__ (self):
        super().__init__ (name = "sliver Sword" , damage_boost = 25 , weapon_type =  "sword", grade = "c", special_effect = " silver warrior")

    def silver_warrior(self, special_effect):
        
        damage =  


class Silver_long_sword(weapon):

    def __init__ (self):
        super().__init__ (name = "silver long Sword" , damage_boost = 30 , weapon_type = "long sword", grade = "c", special_effect = " silver berseker")


class silver_bow(weapon):

    def __init__ (self):
        super().__init__ (name = "silver long Sword" , damage_boost = 30 , weapon_type = "bow", grade = "c", special_effect = " killing spree")
        
class mythic_sword(weapon):

    def __init__ (self):
        super().__init__ (name = "Mythic Sword" , damage_boost = 40 , weapon_type = "sword", grade = "B", special_effect = " warrior spirit")
        
        
class mythic_long_sword(weapon):

    def __init__ (self):
        super().__init__ (name = "Mythic long Sword" , damage_boost = 45 , weapon_type = "long sword", grade = "B", special_effect = " warrior spirit")
    

class Mythic_bow(weapon):

    def __init__ (self):
        super().__init__ (name = "Mythic bow" , damage_boost = 45 , weapon_type = "bow", grade = "B", special_effect = " Inazuma")


class Lunar_sword(weapon):

    def __init__ (self):
        super().__init__ (name = "Lunar sword" , damage_boost = 55 , weapon_type = "sword", grade = "A", special_effect = " Crimson Howl")
        

class Lunar_long_sword(weapon):

    def __init__ (self):
        super().__init__ (name = "Lunar long sword" , damage_boost = 55 , weapon_type = "long sword", grade = "A", special_effect = "Crimson Doom")
        

class Lunar_bow(weapon):

    def __init__ (self):
        super().__init__ (name = "Lunar bow" , damage_boost = 55 , weapon_type = "bow", grade = "A", special_effect = " Crimson hunter")


        
class Phanthom_sword(weapon):

    def __init__ (self):
        super().__init__ (name = "Phanthom bow" , damage_boost = 70 , weapon_type = "sword", grade = "S", special_effect = " Inazuma")



class Phanthom_long_sword(weapon):

    def __init__ (self):
        super().__init__ (name = "Phanthom bow" , damage_boost = 77 , weapon_type = "long sword", grade = "S", special_effect = " Crimson hunter")


class Phanthom_bow(weapon):

    def __init__ (self):
        super().__init__ (name = "Phanthom bow" , damage_boost = 77 , weapon_type = "bow", grade = "S", special_effect = " Crimson hunter")


class Phanthom_crossbow(weapon):

    def __init__ (self):
        super().__init__ (name = "Phanthom crossbow" , damage_boost = 75 , weapon_type = "bow", grade = "S", special_effect = " Crimson hunter")


class Excallibur(weapon):

    def __init__ (self):
        super().__init__ (name = "Excallibur" , damage_boost = 90 , weapon_type = "sword", grade = "S+", special_effect = " Demon killer")

        
class mini_boss (character):

    def __init__(self, name, health, attack, defense, stage):
        super().__init__(name, health, attack, defense)
        self.stage = stage
    

    def level_1_mini_boss (self):

        
        


class enemy(character):
    
    def __init__(self, name, health, attack, defense, stage):
        super().__init__(name, health, attack, defense)
        self.stage = stage
  


class NPC:

    def __init__(self, name, health, items = None, side_quest = None, friendly = True):
        self.name = name
        self.health = health
        self.max_health = health
        self.items = items
        self.side_quest = side_quest
        self.friendly = friendly
        self.is_hostile = False


    def is_alive(self):
        return self.health > 0

    def talk(self, player):

        if self.friendly and not self.is_hostile:
            print(f"{self.name}: Hello {player.name}!")

            if side_quest:
                
                print((f"{self.name}: I have a quest for you adventerer!{self.side_quest['description']}")
                choice = input("Do you accept the quest? (yes/no): ").lower()
                  
                if choice == "yes":
                      player.active_quests.append(self.sidequest)
                      print(f"{self.name}: Thank you! I’ll be waiting.")

                else:
                    
                    print(f"{self.name}: Maybe next time.")  
        else:
            print(f"{self.name} refuses to talk and looks ready to fight!")        


    def attack(self, target):
        damage = 5
        print (f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)

    def take_damage(self,amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage! (HP:{self.health}/{self.max_health})")

        if self.health <= 0:
            print(f"{self.name} has been defeated!")

        else:
            self.is_hostile = True



    def give_items(self, player):
        for item in self.items:
            player.add_to_inventory(item)
            print((f"{self.name} gives you {item.name}")

         self.items.clear()

    def on_defeat(self, player):
        print(f"You loot {self.name}'s items!")
        self.give_items(player)




class HostileNPC(NPC):

    def init(self, name="Rude Villager"):
        
        super().init(name=name, health=20, items=[], sidequest=None)
        self.hostile = True  

    def interact(self, player):
        
        
        print(f"\nAs you walk into the village, a shady figure approaches.")
        print(f"{self.name}: 'Oi! Outsider! You don’t belong here. State your business or prepare to fight!'")

        print("\nWhat do you do?")
        print("1. Intimidate him back.")
        print("2. Try to calm him down.")
        print("3. Say nothing and walk past.")
        print("4. Attack first.")

        choice = input("Choose an action (1/2/3/4): ")
              

        if choice == "1":
              
              print(f"{player.name}: 'Back off before I make you regret it.'")
              print(f"{self.name}: 'Tch... fine, I’m not dying today.' (He backs off.)")

              self.is_hostile = False

        elif choice == "2":
            print(f"{player.name}: 'I don’t want trouble. I’m just passing through.'")
            print(f"{self.name}: '...Hmmm... Fine. But I’ll be watching you.'(He leaves you alone.)")
            
            self.is_hostile = False  

        elif choice == "3":
            
            print(f"{player.name} ignores the NPC and walks past.") 
            print(f"{self.name}: 'Hey! Don’t ignore me!'")
            
            self.start_fight(player)

        elif choice == "4":
            
             
            print(f"{player.name} strikes first!")
            self.start_fight(player)


        else:
            print(f"{self.name}: 'Enough talk , Let’s fight!'")
            self.start_fight(player)
            
    def start_fight(self, player):
        
        print(f"\n{self.name} attacks you!")
        while self.is_alive() and player.is_alive():
            damage = player.attack_value()
            self.take_damage(damage)
            

        if self.is_alive():
            
            player.take_damage(self.attack)

        input()

        if not self.is_alive():
            
            print(f"{self.name} is defeated. He drops nothing of value.")
            
class NPC_01_east_town(NPC):
    
    def __init__(self):
        
        super().__init__(name = "small farmer" , health = 20 , items = None, side_quest = "defeat bandits", friendly = True)

    def interact(self, player):
        print(f"As you walk into the east town, you see a farmer like figure crying in his door steps")
        choice =  input ("do you want to interact with the farmer? (yes/no)").lower()

        if choice == "yes":
            print("you are approaching the farmer, farmer looking at you with a desperate face")
            print(" Farmer stood up in his place and approching you")
            print(f"{self.name} : hello beautiful knight !, please help me ! (farmer started to crying again")
            print(f"{player.name}: what happen to you?")
            print(f"{self.name} : so when i was carrying my loot truck i was attacked by the trickster bandits")
            print(f"{self.name}: i begged  them to spare me and my goods but they took everything from me even my daughter.... ( farmer started crying again like a pathetic figure")
            print(f"{self.name}: pleasee adventurerr pleasee.. help mee... please rescue my sweet daughter and my goods.. she is my life! farmer grabbed her feet, kneel down and started begging")

            print(f" {player.name}:(thinking)(hmm... poor farmer.. should i help him...?)")
            choice_01 = input ("do u accept the request?: (yes/no)").lower()

            if choice_01 == "yes":
                print("you have accepted the farmer's quest !")
                print(f"{self.name}: Thank you so much my life savier knight ! please bring my daughter back safely! hope u good luck !")
                print(f" {player.name}: (thinking: he is cringy but yeah any father would do the same i guess)  {player.name} nodd the farmer and get ready to leave")
                print(f" suddenly the farmer approached {player.name}and {self.name}: before you go i have some advices to aware of, bandits always hiding in very rocky places ! always cross the road with obstacle and slow down anyone going in the road so be careful {player.name}:")
                print(f" {player.name}: Interesting ! thank you for the advice will look out for it !, {player.name} gave a friendly smile to the farmer and left the town.")
                defeat_bandits.showobstacles(player)
                
            if choice_01 == "No":
                print(" You didnt accept the quest, you can come again later to accept the quest")
                print(f"{player.name}: walked away from the farmer)

            


defeat_bandits = (" Rescue the villages from the bandits", bandits = [bandit_01,bandit_02, bandit_03, bandit_04, bandit_05 ]
class defeat_bandits:

    def __init__(self, name =  , bandits):
        self.name = name (" Rescue the villages from the bandits")
        self.bandits = bandits [bandit_01,bandit_02, bandit_03, bandit_04, bandit_05 ]


        self.obstacles = ["Fallen logs", "big stone"]


        def show_obstacles(self, player):
            print("\nObstacles in the road")

            print(f" there are {self.obstacles[0]} in front of the road")
            print(f" to get the pass the obstacle u need to cut down {self.obstacles[0]}!")
            choice = input( " Use the axe to cut down the {self.obstacles[0]} to get passed it!:").lower()

            if choice == "axe":
                player.equip.(axe)

                choice_01 = input ("press any button to cut {self.obstacles[0]}:").lower()
                
                if choice_01 == input():
                    print(" you have cut down the self.obstacles[0]} and cleared the road !")
                    self.obstacles.pop[0]


                    
            print("\nAnother obstacles in the road")
            print(f" there are {self.obstacles[1]} in front of the road")
            print(f" to get the pass the obstacle u need to push the {self.obstacles[0]}out of the road")

            choice_02 = input ("press any button to push the {self.obstacles[0]}:").lower()

            if choice_02 == input():
                 self.encounter_theifs(player)
                

        def encounter_thiefs(self, player):

            print(f"\n Suddenly a group of people who wearing a cameo color suits came out of nowhere !! and surrounded the {player.name}!!! ")
            print(f" {player.name}: (thinking) Thiefs are exactly matches the description of farmer saying huh.... she was thinking this while keeping her eye contact with the strangers")
            print(f" {self.bandits.name[0]}: Hoooo ! this time we hit the jackpot guyss !! its a beautiful lady knight !!/ one bandit saying this while looking at {player.name}")
            print(f" bandit group laughed very sarcastically !")
            print(f" {self.bandits.name} : hey princess would you like to give us your precious belonging here please? ( one bandit ask {player.name} while licking his knife ")
            
            options = [
                
                "1. 'This is your worst day bandits ! iam here to kick your asses!.'",
                "2. 'I’m just passing by, I want no trouble.'",
                "3. 'Iam looking for a small child'"
               ]
            
            while True:
                
                for opt in options:
                    print(opt)
                    
                choice = input("Choose your response (1-3): ")



                if choice == "1":
                    print(f" {self.bandits.name[3]}: ohh you are going to get hurt sweet lady "')
                    self.trigger_battle_bandits(player)
                    break

                if choice == "2":
                    print(f"{self.bandits.name[3]}: hahaha !( laughed sarcastically!) you are going no where lady unless you give what we wants")
                    print(f"{self.bandits.name[2]}: We ask u one more time,  Give your belongings lady or else u are going to get hurt")

                    options_1 = [ "1. 'Fuck you Assholes ! iam not giving anything! ( draws your weapon!)'",
                                "2. 'Okay This is what i have' ( thiefs get your armor and your weapons) ",
                            ]
                    
                    for opt in options_1:
                        
                        print(opt)
                    
                    choice_01 = input ("Choose your response (1-2): ")


                    if choice_01 =="1":
                        self.trigger_battle_bandits(player)
                        break

                    if choice_01 == "2":
                        print(f" {player.name}lost the armor and weapon")
                        print(f" {self.bandits.name[4]}: Our lucky dayy ! We got some valuable armor from a knight ! how humiliating ! ( theifs started to laugh very loudly)")
                        print(f" theifs vanished into the forest")
                        print(" You failed the Quest!")

                if choice == "3":
                    print(f" {self.bandits.name[3]} haha to know about her you have to defeat us ! but thats not gonna happen haha!")
                    print(f" {player.name}: Very well then, I could warm up with you guys")
                    self.trigger_battle_bandits(player)
                    break

        def trigger_battle_bandits (self, player):

            bandit_01 = enemy("bandit 01", health = 35, attack = 12, defense = 5, stage = 2),
            bandit_02 = enemy("bandit 02", health = 35, attack = 10, defense = 5, stage = 2),
            bandit_03 = enemy("bandit 03", health = 35, attack = 9, defense = 5, stage = 2),
            bandit_04 = enemy("bandit 04", health = 35, attack = 11, defense = 5, stage = 2),
            bandit_05 = enemy("bandit 05", health = 35, attack = 12, defense = 5, stage = 2),
            
            
            print("\n  -----Combat Starts-----")

            target = 0
            
            while any(self.bandits.is_alive() for bandits in self.bandits) and player.is_alive():
                print("\nYour Turn:")
                
                cmd = input("\nYour move: ").lower()

                if cmd.startswith("target"):
                    
                    if "1" in cmd:
                        target = 0

                    elif "2" in cmd:
                        target = 1
                    
                    elif "3" in cmd:
                        target = 2
                        
                    elif "4" in cmd:
                        target = 3
                        
                    elif "5" in cmd:
                        target = 4
                        
                    print(f"You focus on {self.bandits[target].name}")
                    
                elif cmd == "attack":
                    if self.bandits[target].is_alive():
                        damage = player.attack_value()
                        self.bandits[target].take_damage(damage)

                        if not self.bandits[target].is_alive():
                            
                            print(f"{self.bandits[target].name} is defeated!")

                    else:
                        print("Bandit is already down")

                elif cmd == "block":
                    print("You brace yourself for incoming attacks. Damage will be halved.")
                    player.defense += 5
                    
                    for bandits in self.bandits:
                        if bandits.is_alive():
                            player.take_damage(bandits.attack // 2)

                    continue

                elif cmd = "run":
                    print ("you can't run from this fight")

                else:
                    print("Invalid command")

                for bandits in self.bandits:
                    
                    if bandits.is_alive():
                        player.take_damage(bandits.attack)

                player.defense = max(10, player.defense - 5)  # Reset block boost
                
            if player.is_alive():
                print("You defeated the thiefs!")

                money_pouch = Item("Farmer's money pouch", "Farmer's stolen valuables")
                Batch_bandits = Item ("trickster Bandit batch"," A trophy for defeating trickster bandits")
                player.add_to_inventory(money_pouch)
                player.add_to_inventory(Batch_bandits)
    
            
class npc_01west_town:

    super().__init__(name = "old man with a weird moushtache" , health = 20 , items = None, side_quest = "defeat bandits", friendly = True)

    def interact (self, player):
        print(f" 

            

class destroyed_town:

    def __init__(self, name):
        self.name = "destroyed town"


    def starting_a_event(self, player):
        print(f" As {player.name} wallking in the forest path , she sees a ruins of a huge town which she observed it miles away")
        print(f"{player.name} : ehh is it a very old battle place ??? interesting ! i need to get a look closer and see what it is really")
        print(f"{player.name} started to walk towards the unindentified place...")
        print(f" after a closer a look it was a town that got destroyed ")
        print(f" {player.name}: ( thinking to herself) these damages look like it happened recently, what in a hell actually happened here.... all of the houses, shops are burned and only foundation remains... {player.name} thinks to her self very shockingly")
        print(f" {player.name}: I need to investigate this, iam getting pretty curious about this...to get every house into the ground !! this kind of destruction was wayy off limits of our army or even for a bandits..")
        print(f" {player.name} started to walk cross the destroyed buildings")
        print(f" {player.name}: looks like its not a normal damage, seems like someone cast a spell and did magic damage she was thinking this looking around a destroyed buildings in the town")
        print(f" {player.name}  who in the hell attacked them.. OHH i remembers this town ! this town known to be the 'dragons who walks the heaven', and this town had very astonishing art work historically valued that aged upto king arthur's era as i remembers")
        print(f" {player.name}: seems like everything being burned to ashes.. 


























































































        
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




    
    
            
        
