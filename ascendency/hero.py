import json

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
        print("--- STATS DE l'HERO ---")
        print("Name : ",self.name)
        print("PV : ",self.pv)
        print("Defense : ",self.defense)
        print("Attack : ",self.attack)
        print("Mana :", self.mana,"(Un hero n'a pas de mana)")
        print("Dodge :", self.dodge,"(Un hero n'a pas de dodge)")

    
    def equip_item(self, item):
        with open('Gears/weapons.json', 'r', encoding='utf-8') as file:
            weapons_list = json.load(file)

        with open('Gears/armors.json', 'r', encoding='utf-8') as file:
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