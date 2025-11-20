from menu import pvp
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
        print("Mode PvE en cours de maintenance (bientôt disponible)")
display_menu()