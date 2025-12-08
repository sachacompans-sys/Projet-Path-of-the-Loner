import json
import random
import os


class Hero_class:
    def __init__(self, name: str = "Hero", pv: int = 1000, defense: int = 0, attack: int = 0, mana: int = 0, dodge: int = 0, gold: int = 0):
        self.name = name
        self.pv = pv
        self.defense = defense
        self.attack = attack
        self.mana = mana
        self.dodge = dodge
        self.gold = gold

    def display(self):
        self.dice_roll()

    def dice_roll(self):
        from Gears.armor import Armor
        from Gears.weapons import Weapon
        
        print()
        print(f"--- STATS ---")
        print(f"Défense : {self.defense} | Attaque : {self.attack}")
        print()
        
        input("Lancer le dé pour votre armure ->")
        dice_value_armor = random.randint(1, 100)
        print(f"Résultat du dé : {dice_value_armor}")
        
        armor_system = Armor()
        available_armors = armor_system.read_Armor(dice_value_armor)
        armor_system.choice_in_rarity(available_armors, self)
        
        print()
        input("Lancer le dé pour votre arme ->")
        dice_value_weapon = random.randint(1, 100)
        print(f"Résultat du dé : {dice_value_weapon}")
        
        weapon_system = Weapon()
        available_weapons = weapon_system.read_Weapon(dice_value_weapon)
        weapon_system.choice_in_rarity(available_weapons, self)
        
        print()
        print(f"--- STATS ---")
        print(f"Défense : {self.defense} | Attaque : {self.attack}")

    def equip_item(self, item):
        base_path = os.path.dirname(os.path.dirname(__file__))
        weapons_path = os.path.join(base_path, 'Gears', 'weapons.json')
        armors_path = os.path.join(base_path, 'Gears', 'armor.json')
        
        with open(weapons_path, 'r', encoding='utf-8') as file:
            weapons_list = json.load(file)

        with open(armors_path, 'r', encoding='utf-8') as file:
            armors_list = json.load(file)
       
        print(f"--> Vous equipez : {item['name']}")
        
        if 'damage' in item:
            bonus = item['damage']
            self.attack = self.attack + bonus
            print(f"Vos degats augmentent de +{bonus} ! (Attaque actuelle : {self.attack})")
            
        elif 'defense' in item:
            bonus = item['defense']
            self.defense = self.defense + bonus
            print(f"Votre defense augmente de +{bonus} ! (Defense actuelle : {self.defense})")


if __name__ == "__main__":
    hero = Hero_class()
    hero.display()