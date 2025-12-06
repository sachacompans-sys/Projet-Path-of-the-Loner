class Hero_class:
    def __init__(self, name: str = "Hero", pv: int = 1000, defense: int = 0, attack: int = 0, mana: int = 0, dodge: int = 0, gold: int = 0):
        self.name = name
        self.pv = pv
        self.defense = defense
        self.attack = attack
        self.mana = mana
        self.dodge = dodge
        self.gold = gold

#Affichage stats, input Equipement
    def affichage(self):
        print("--- STATS DE l'HERO ---")
        print("Name : ",self.name)
        print("PV : ",self.pv)
        print("Defense : ",self.defense)
        print("Attack : ",self.attack)
        print("Mana :", self.mana,"(Un hero n'a pas de mana)")
        print("Dodge :", self.dodge,"(Un hero n'a pas de dodge)")