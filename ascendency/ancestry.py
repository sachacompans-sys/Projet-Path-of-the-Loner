class Archère:
    def __init__(self, name: str, pv: int, defense: int, attack: int, mana: int, dodge: int):
        self.name = name
        self.pv = pv
        self.defense = defense
        self.attack = attack
        self.mana = mana
        self.dodge = dodge
    
    def affichage(self):
        print("--- STATS DE l'ARCHERE ---")
        print("Name : ",self.name)
        print("PV : ",self.pv)
        print("Defense : ",self.defense)
        print("Attack : ",self.attack)
        print("Mana :", self.mana,"(Un hero n'a pas de mana)")
        print("Dodge :", self.dodge)

class Guerrier:
    def __init__(self, name: str, pv: int, defense: int, attack: int, mana: int, dodge: int):
        self.name = name
        self.pv = pv
        self.defense = defense
        self.attack = attack
        self.mana = mana
        self.dodge = dodge
    
    def affichage(self):
        print("--- STATS DU GUERRIER ---")
        print("Name : ",self.name)
        print("PV : ",self.pv)
        print("Defense : ",self.defense)
        print("Attack : ",self.attack)
        print("Mana :", self.mana,"(Un hero n'a pas de mana)")
        print("Dodge :", self.dodge, "(Un hero n'a pas de dodge)")

class Magicienne:
    def __init__(self, name: str, pv: int, defense: int, attack: int, mana: int, dodge: int):
        self.name = name
        self.pv = pv
        self.defense = defense
        self.attack = attack
        self.mana = mana
        self.dodge = dodge

    def affichage(self):
        print("--- STATS DU MAGICIENNE ---")
        print("Name : ",self.name)
        print("PV : ",self.pv)
        print("Defense : ",self.defense)
        print("Attack : ",self.attack)
        print("Mana :", self.mana)
        print("Dodge :", self.dodge, "(Un hero n'a pas de dodge)")