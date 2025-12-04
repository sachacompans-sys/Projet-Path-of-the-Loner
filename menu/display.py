from . import pvp
from . import pve
import os

def display_menu():
    print()
    input("---------- Bienvenue dans Path of the Loner ----------")
    print()
    pvp_or_pve = input("Souhaitez-vous jouer en PvP(1) ou Pve(2) : ")
    if pvp_or_pve == "1" :
        os.system('cls')
        session = pvp.opponent()
        session.choice()
    else:
        os.system('cls')
        session = pve.characters()
        session.choice()
display_menu()