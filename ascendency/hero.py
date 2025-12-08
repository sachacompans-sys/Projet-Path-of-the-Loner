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


if __name__ == "__main__":
    hero = Hero_class()
    hero.display()