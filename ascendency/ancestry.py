import json
from menu import pvp



class Archer:
    def __init__(self, name: str = "", pv: int = 0, defense: int= 0, attack: int = 0, mana: int= 0, dodge: int = 0, gold: int = 0):
        self.name = name
        self.pv = pv
        self.defense = defense
        self.attack = attack
        self.mana = mana
        self.dodge = dodge
        self.gold = gold
    
    def load_stats_archer(self):
        with open('ascendency/ancestry.json', 'r', encoding='utf-8') as file:
            list_data = json.load(file)   
        stats_dict = list_data[0]    
        
        self.name = stats_dict['name']
        self.pv = stats_dict['pv']
        self.defense = stats_dict['defense']
        self.attack = stats_dict['attack']
        self.mana = stats_dict['mana']
        self.dodge = stats_dict['dodge']
        self.gold = stats_dict['gold']
        
        print("--- STATS DE l'ARCHERE ---")

        print("Name : ",self.name)
        print("PV : ",self.pv)
        print("Defense : ",self.defense)
        print("Attack : ",self.attack)
        print("Mana :", self.mana,"(Un hero n'a pas de mana)")
        print("Dodge :", self.dodge)

class Warrior:
    def __init__(self, name: str = "", pv: int = 0, defense: int= 0, attack: int = 0, mana: int= 0, dodge: int = 0, gold: int = 0):
        self.name = name
        self.pv = pv
        self.defense = defense
        self.attack = attack
        self.mana = mana
        self.dodge = dodge
        self.gold = gold

    def load_stats_warrior(self):
        with open('ascendency/ancestry.json', 'r', encoding='utf-8') as file:
            list_data = json.load(file)
        stats_dict = list_data[1]    

        
        self.name = stats_dict['name']
        self.pv = stats_dict['pv']
        self.defense = stats_dict['defense']
        self.attack = stats_dict['attack']
        self.mana = stats_dict['mana']
        self.dodge = stats_dict['dodge']
        self.gold = stats_dict['gold']
        
        print("--- STATS DU GUERRIER ---")

        print("Name : ",self.name)
        print("PV : ",self.pv)
        print("Defense : ",self.defense)
        print("Attack : ",self.attack)
        print("Mana :", self.mana,"(Un guerrier n'a pas de mana)")
        print("Dodge :", self.dodge,"(Un guerrier n'a pas de chance de dodge)")
    

class Magician:
    def __init__(self, name: str = "", pv: int = 0, defense: int= 0, attack: int = 0, mana: int= 0, dodge: int = 0, gold: int = 0):
        self.name = name
        self.pv = pv
        self.defense = defense
        self.attack = attack
        self.mana = mana
        self.dodge = dodge
        self.gold = gold

    def load_stats_magician(self):
        with open('ascendency/ancestry.json', 'r', encoding='utf-8') as file:
            list_data = json.load(file)
        stats_dict = list_data[2]        
        
        self.name = stats_dict['name']
        self.pv = stats_dict['pv']
        self.defense = stats_dict['defense']
        self.attack = stats_dict['attack']
        self.mana = stats_dict['mana']
        self.dodge = stats_dict['dodge']
        self.gold = stats_dict['gold']
        
        print("--- STATS DE LA MAGICIENNE ---")

        print("Name : ",self.name)
        print("PV : ",self.pv)
        print("Defense : ",self.defense)
        print("Attack : ",self.attack)
        print("Mana :", self.mana)
        print("Dodge :", self.dodge,"(Une magicienne n'a pas de chance de dodge)")

 
