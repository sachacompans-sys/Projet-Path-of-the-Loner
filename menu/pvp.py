import random
from time import sleep
import os
import sys

# Import des classes du jeu
from ascendency.hero import Hero_class
from ascendency.ancestry import Archer, Warrior, Magician

class opponent: 
    def __init__(self):
        self.player_hero = None

    def choice(self):
        """Permet au joueur de choisir son héros et d'équiper son stuff (via display())."""
        print("------------------- MODE PvP -------------------\n")
        sleep(0.5)
        print("--- CRÉATION DU PERSONNAGE ---\n")
        sleep(0.5)
        
        while self.player_hero is None:
            choice_player1 = input ("choisis ton Héro ou une ascendance : hero(1) / archère(2) / guerrier(3) / magicienne(4) : ")
            print()
            
            if choice_player1 == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("-> Tu as choisi le Héro !\n")
                self.player_hero = Hero_class(name="Joueur")
                self.player_hero.display()
                sleep(2)
                self.start_combat()
            elif choice_player1 == "2": 
                os.system('cls' if os.name == 'nt' else 'clear')
                print("-> Tu as choisi l'Archère !\n")
                self.player_hero = Archer(name="Archère Joueur")
                self.player_hero.load_stats_archer()
                self.player_hero.display() 
            elif choice_player1 == "3": 
                os.system('cls' if os.name == 'nt' else 'clear')
                print("-> Tu as choisi le Guerrier !\n")
                self.player_hero = Warrior(name="Guerrier Joueur")
                self.player_hero.load_stats_warrior()
                self.player_hero.display() 
            elif choice_player1 == "4": 
                os.system('cls' if os.name == 'nt' else 'clear')
                print("-> Tu as choisi la Magicienne !\n")
                self.player_hero = Magician(name="Magicienne Joueur")
                self.player_hero.load_stats_magician()
                self.player_hero.display() 
            else:
                print("Choix invalide, veuillez réessayer.")
        
        print("\n--- Équipement terminé. Préparez-vous au combat ! ---")
        sleep(2)

    def generate_opponent(self):

        opponent_ia = Hero_class(name="Adversaire Fantôme")

        total_points = random.randint(30, 60)
        attack_points = random.randint(5, total_points // 2)
        defense_points = random.randint(5, total_points - attack_points)
        
        opponent_ia.pv = random.randint(900, 1000)
        opponent_ia.defense = defense_points
        opponent_ia.attack = attack_points
        
        return opponent_ia

    def start_combat(self):
        
        if self.player_hero is None:
            self.choice()
            
        opponent_ia = self.generate_opponent()

        damage_player_to_ia = max(1, self.player_hero.attack - opponent_ia.defense)
  
        damage_ia_to_player = max(1, opponent_ia.attack - self.player_hero.defense)
        
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("=============================================")
        print(f"COMMENCEMENT DU COMBAT : {self.player_hero.name} vs {opponent_ia.name}")
        print("=============================================")
        sleep(1.5)
        
        print(f"\n--- STATS INITIALES ---")
        print(f"{self.player_hero.name} : PV {self.player_hero.pv} | ATK {self.player_hero.attack} | DEF {self.player_hero.defense} | Dégâts constants: {damage_player_to_ia}")
        print(f"{opponent_ia.name} : PV {opponent_ia.pv} | ATK {opponent_ia.attack} | DEF {opponent_ia.defense} | Dégâts constants: {damage_ia_to_player}")
        sleep(3)
        
        current_turn = 1
        
        while self.player_hero.pv > 0 and opponent_ia.pv > 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"--- TOUR {current_turn} ---")
            print(f"PV {self.player_hero.name}: {self.player_hero.pv} | PV {opponent_ia.name}: {opponent_ia.pv}")
            print("-" * 15)
            
      
            input("Appuyez sur Entrée pour attaquer...")

            damage_to_opponent = damage_player_to_ia 
            
            opponent_ia.pv -= damage_to_opponent
            print(f"{self.player_hero.name} attaque. Dommages infligés à {opponent_ia.name} : {damage_to_opponent}")
            sleep(1.5)
            
            if opponent_ia.pv <= 0:
                break

            damage_to_player = damage_ia_to_player 
            
            self.player_hero.pv -= damage_to_player
            print(f"{opponent_ia.name} contre-attaque. Dommages subis par {self.player_hero.name} : {damage_to_player}")
            sleep(1.5)
            
            current_turn += 1

        print("\n=============================================")
        if self.player_hero.pv > 0:
            print(f"VICTOIRE ! {self.player_hero.name} a vaincu {opponent_ia.name}.")
            gain_gold = random.randint(10, 50)
            self.player_hero.gold += gain_gold
            print(f"Vous gagnez {gain_gold} pièces d'or ! Total : {self.player_hero.gold}")
        else:
            print(f"DÉFAITE ! {self.player_hero.name} a été vaincu par {opponent_ia.name}.")
        print("=============================================")
        input("Appuyez sur Entrée pour continuer...")


if __name__ == "__main__":
    session = opponent()
    session.start_combat()