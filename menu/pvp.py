from time import sleep
from ascendency.hero import Hero_class
from ascendency.ancestry import Archer, Warrior, Magician
import os


class opponent:
    def __init__(self, name: str="waiting", pv: int=1000, defense: int=0, attack: int=0, mana: int = 0, dodge: int = 0):
        self.name = name
        self.pv = pv
        self.defense = defense
        self.attack = attack
        self.mana = mana
        self.dodge = dodge
    

    def choice(self):
        print("------------------- MODE PvP -------------------\n")
        sleep(0.5)
        print("--- CRÉATION DU PERSONNAGE ---\n")
        sleep(0.5)
        choice_player1 = input ("choisis ton Héro ou une ascendance : hero(1) / archère(2) / guerrier(3) / magicienne(4) : ")
        print()
        if choice_player1 == "1":
            os.system('cls')
            print("-> Tu as choisi le Héro !\n")
            selection_hero = Hero_class()
            selection_hero.display()
        elif choice_player1 == "2": 
            os.system('cls')
            print("-> Tu as choisi le L'Archère !\n")
            selection_hero = Archer()
            selection_hero.load_stats_archer()
        elif choice_player1 == "3": 
            os.system('cls')
            print("-> Tu as choisi le Guerrier !\n")
            selection_hero = Warrior()
            selection_hero.load_stats_warrior()
        elif choice_player1 == "4": 
            os.system('cls')
            print("-> Tu as choisi la Magicienne !\n")
            selection_hero = Magician()
            selection_hero.load_stats_magician()