import json 

class Pvp:
    def __init__(self, player1:int, player2:int):
        self.player1 = player1
        self.player2 = player2
    

def choice(self):
    choice_player1 = input ("choisis ton Héro ou une ascendance : (hero(1) / archère(2) / guerrier(3) / magicienne(4))")
    if choice_player1 == "hero":
        weapon_choice  = input("choisis ton arme :")
        armor_choice = input("choisis ton armure :")
    if choice_player1 == "archère":
        print("ta choisis l\'archère")
    if choice_player1 == "guerrier":
        print("ta choisis le guerrier")
    if choice_player1 == "magicienne":
        print("ta choisis la magicienne")
