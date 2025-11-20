import pvp

def display_menu():
    input("-----------Bienvenue dans Path of the Loner-----------")
    pvp_or_pve = input("Souhaitez-vous jouer en PvP(1) ou Pve(2) :")
    if pvp_or_pve == "1" :
        pvp.choice()
    else:
        print("Mode PvE en cours de maintenance (bientôt disponible)")

display_menu()