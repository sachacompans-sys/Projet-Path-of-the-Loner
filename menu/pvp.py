import ascendency

class Player1:
    def __init__(self, nom: str, pv: int, defense: int, attack: int, mana: int = 0, dodge: int = 0):
        self.nom = nom
        self.pv = pv
        self.defense = defense
        self.attack = attack
        self.mana = mana
        self.dodge = dodge

class Player2:
    def __init__(self, nom: str, pv: int, defense: int, attack: int, mana: int = 0, dodge: int = 0):
        self.nom = nom
        self.pv = pv
        self.defense = defense
        self.attack = attack
        self.mana = mana
        self.dodge = dodge
    

def choice(self):
    input("--- CRÉATION DU PERSONNAGE ---")
    choice_player1 = input ("choisis ton Héro ou une ascendance : (hero(1) / archère(2) / guerrier(3) / magicienne(4))")
    if choice_player1 == "1" :
        ascendency.hero()
    if choice_player1 == "2" :
        print("ta choisis l\'archère")
    if choice_player1 == "3" :
        print("ta choisis le guerrier")
    if choice_player1 == "4" :
        print("ta choisis la magicienne")

def hero(self):



choice()