import os

def display_menu():
    print()
    input("---------- Bienvenue dans Path of the Loner ----------")
    print()
    pvp_or_pve = input("Souhaitez-vous jouer en PvP(1) ou Pve(2) : ")
    if pvp_or_pve == "1":
        os.system('cls')
        from menu.pvp import opponent
        session = opponent()
        session.choice()
    else:
        os.system('cls')
        from menu.pve import characters
        session = characters()
        session.choice()

if __name__ == "__main__":
    display_menu()