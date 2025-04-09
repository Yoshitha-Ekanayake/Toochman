from character import hero,enemy
from weapons import short_bow,iron_sword
import random

hero = hero(name = "hero", health = 100 )
hero.equip(iron_sword)
enemy = enemy(name = "enemy", health = 100, weapon = short_bow)

#hero = Character(name = "hero", health = 100, damage =random.randrange( 11, 14))
#enemy = Character(name = "enemy", health = 100, damage = random.randrange( 10, 13))



while True:
    
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"health of {hero.name} : { hero.health}")
    
    print(f"health of {enemy.name} : { enemy.health}")

    hero.drop(iron_sword)
    input()
    
    if hero.health == 00 and enemy.health == 00 :   
        print("hurray")
        break
    



    
