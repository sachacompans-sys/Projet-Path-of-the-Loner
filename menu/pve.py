from time import sleep
from ascendency import hero
from ascendency import ancestry
import os
import random

class characters:
    def __init__(self, name: str="waiting", pv: int=1000, defense: int=0, attack: int=0, mana: int = 0, dodge: int = 0):
        self.name = name
        self.pv = pv
        self.defense = defense
        self.attack = attack
        self.mana = mana
        self.dodge = dodge
    

    def choice(self):
        print("------------------- MODE PvE -------------------\n")
        sleep(0.5)
        print("--- CRÉATION DU PERSONNAGE ---\n")
        sleep(0.5)
        choice_player1 = input ("choisis ton Héro ou une ascendance : hero(1) / archère(2) / guerrier(3) / magicienne(4) : ")
        print()
        if choice_player1 == "1" :
            os.system('cls')
            print("-> Tu as choisi le Héro !\n")
            selection_hero = hero.Hero_class()
            selection_hero.affichage()
        elif choice_player1 == "2" : 
            os.system('cls')
            print("-> Tu as choisi le L'Archère !\n")
            selection_hero = ancestry.Archer()
            selection_hero.load_stats_archer()
        elif choice_player1 == "3" : 
            os.system('cls')
            print("-> Tu as choisi le Guerrier !\n")
            selection_hero = ancestry.Warrior()
            selection_hero.load_stats_warrior()
        elif choice_player1 == "4" : 
            os.system('cls')
            print("-> Tu as choisi la Magicienne !\n")
            selection_hero = ancestry.Magician()
            selection_hero.load_stats_magician()                
        
#combat modulaire systeme

class Weapon:
    def __init__(self, name, damage, bonus):
        self.name = name
        self.damage = damage
        self.bonus = bonus

class Character:
    def __init__(self, name:str, hp:int):
        self.hp = hp
        self.name = name
        self.weapon = None 
        self.priority = 0

    def weapon_equiped(self, weapon_n:str):
        with open('weapons.json', 'r') as f:
            all_weapon = json.load(f)
            for weapons in all_weapon:
                if weapons["name"] == weapon_n:
                    self.weapon = Weapon(weapons["name"], weapons["damage"], weapons["bonus"])
                    return
    
    def attack_openent(self, enemy:Character):
        enemy.hp -= self.weapon.damage
        print(f"vous vennez d'ingligé {self.weapon.damage}degas il reste actuelement {enemy.hp}HP a votre adversaire")

class Warrior(Character):
    def __init__(self, name:str, hp:int):
         super().__init__(name, hp)
         self.character_class = "Warrior"
         self.priority = 0
    
    def attack_openent(self, enemy:Character):
        enemy.hp -= self.weapon.damage
        print(f"vous vennez d'ingligé -{self.weapon.damage}degas")
        enemy.hp -= self.weapon.damage
        print(f"vous ingligé un coup -{self.weapon.damage}degas il reste actuelement {enemy.hp}HP a votre adversaire")


class Archer(Character):
    def __init__(self, name, hp):
        super().__init__(name, hp)

        self.character_class = "Archer"
        self.dodge_chance = 0.25
        self.priority = 100
        
    def attack_openent(self, enemy:Character):
        enemy.hp -= self.weapon.damage
        print(f"vous vennez d'ingligé -{self.weapon.damage}degas il reste actuelement {enemy.hp}HP a votre adversaire")

    def dodge_attack(self, damage: float):
        if random.random() < self.dodge_chance:
            print("vous vous vennez d'esquiver l'attaque")
            return 0
        else:
            if self.armor:
                damage = max(0, damage - self.armor.defense)
            self.hp -= damage
            return damage

class Mage(Character):
    def __init__(self, name:str, hp:int):
        super().__init__(name, hp)
        self.character_class = "Mage"
        self.mana = 100
        self.priority = 0
    
    def attack_openent(self, enemy:Character):
        choice = input("vous vouler attaquer avec votre arme ou lancer un sort ? (arme/sort) : ")
        
        if choice == "arme":
            enemy.hp -= self.weapon.damage
            print(f"vous vennez d'ingligé {self.weapon.damage}degas il reste actuelement {enemy.hp}HP a votre adversaire")
        
        elif choice == "sort":
            if self.mana >= self.sort.mana:
                self.mana -= self.sort.mana
                enemy.hp -= self.sort.degas
                print(f"vous vennez de lancer un sort et ingligé 30degas il reste actuelement {enemy.hp}HP a votre adversaire")
                print(f"il vous reste {self.mana}mana")
            else:
                print("vous n'avez pas assez de mana")