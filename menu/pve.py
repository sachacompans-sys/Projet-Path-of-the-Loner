import os
import time
import random

from ascendency import hero, ancestry
from Gears.armor import Armor
from Gears.weapons import Weapon
from PvE.room import Room
from PvE.loot import get_loot

try:
    from PvE.merchants import City_path
except ImportError:
    print("Erreur: merchants.py introuvable.")
    City_path = None

class characters:
    def __init__(self, name: str="waiting", pv: int=1000, defense: int=0, attack: int=0, mana: int = 0, dodge: int = 0):
        self.name = name
        self.pv = pv
        self.defense = defense
        self.attack = attack
        self.mana = mana
        self.dodge = dodge

    def choice(self):
        print("------------------- MODE PvE -------------------\n")
        time.sleep(0.5)
        print("--- CREATION DU PERSONNAGE ---\n")
        time.sleep(0.5)
        
        player_choice = input("Choisis ton Hero ou une ascendance : hero(1) / archere(2) / guerrier(3) / magicienne(4) : ")
        print()
        
        selected_hero = None

        if player_choice == "1" :
            os.system('cls' if os.name == 'nt' else 'clear')
            print("-> Tu as choisi le Hero (Classique) !\n")
            selected_hero = hero.Hero_class()
            selected_hero.affichage()
            
        elif player_choice == "2" : 
            os.system('cls' if os.name == 'nt' else 'clear')
            print("-> Tu as choisi l'Archere (Haute Esquive) !\n")
            selected_hero = ancestry.Archer()
            selected_hero.load_stats_archer()
            if not hasattr(selected_hero, 'dodge'): selected_hero.dodge = 20
            self.starting_equipment(selected_hero)
            
        elif player_choice == "3" : 
            os.system('cls' if os.name == 'nt' else 'clear')
            print("-> Tu as choisi le Guerrier (Haute Defense) !\n")
            selected_hero = ancestry.Warrior()
            selected_hero.load_stats_warrior()
            selected_hero.mana = 0
            self.starting_equipment(selected_hero)
            
        elif player_choice == "4" : 
            os.system('cls' if os.name == 'nt' else 'clear')
            print("-> Tu as choisi la Magicienne (Mana & Sorts) !\n")
            selected_hero = ancestry.Magician()
            selected_hero.load_stats_magician()
            if not hasattr(selected_hero, 'mana'): selected_hero.mana = 100
            self.starting_equipment(selected_hero)
        
        else:
            print("Choix invalide, selection du Hero par defaut.")
            selected_hero = hero.Hero_class()

        if selected_hero:
            self.open_shop(selected_hero)
            
            input("\nAppuyez sur Entree pour entrer dans le donjon...")
            self.start_adventure(selected_hero)

    def open_shop(self, player):
        if City_path:
            input(f"\nAppuyez sur Entree pour acceder au Marchand...")
            boutique = City_path(player.name, 135, 10)
            boutique.city()
        else:
            print("Le marchand est absent (Fichier manquant).")

    def starting_equipment(self, player):
        print("\n--- EQUIPEMENT DE DEPART ---")
        
        input("Lancer le de pour votre ARMURE -> ")
        dice = random.randint(1, 100)
        armor_system = Armor()
        armor_list = armor_system.read_Armor(dice) 
        armor_system.choice_in_rarity(armor_list, player)
        
        input("\nLancer le de pour votre ARME -> ")
        dice = random.randint(1, 100)
        weapon_system = Weapon()
        weapon_list = weapon_system.read_Weapon(dice)
        weapon_system.choice_in_rarity(weapon_list, player)
        
        print("\nVous etes pret au combat !")
        time.sleep(1)

    def start_adventure(self, player):
        room_manager = Room()

        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- SALLE A (Normal) ---")
        monster = room_manager.get_normal_room()
        
        if self.combat_loop(player, monster) == False: return 
        self.handle_loot(player, "Normal")

        self.open_shop(player)

        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- SALLE B (Elite) ---")
        monster = room_manager.get_elite_room()
        
        if self.combat_loop(player, monster) == False: return
        self.handle_loot(player, "Elite")

        self.open_shop(player)

        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- SALLE C (BOSS) ---")
        monster = room_manager.get_boss_room()
        
        if self.combat_loop(player, monster) == False: return
        self.handle_loot(player, "Boss")

        print("\n" + "="*40)
        print("VICTOIRE ! Vous avez fini le couloir des defunts.")
        print("="*40)
        input("Appuyez sur Entree pour quitter...")

    def combat_loop(self, player, monster):
        print(f"\nDEBUT DU COMBAT : {player.name} vs {monster.name}")
        
        while player.pv > 0 and monster.hp > 0:
            stats_line = f"[VOUS] PV: {int(player.pv)} | ATK: {player.attack} | DEF: {player.defense}"
            
            if hasattr(player, 'mana') and player.mana > 0:
                stats_line += f" | MANA: {player.mana}"
            
            if hasattr(player, 'dodge') and player.dodge > 0:
                stats_line += f" | ESQUIVE: {player.dodge}%"
                
            print(f"\n{stats_line}")
            print(f"[ENNEMI] PV: {monster.hp} | DEGATS: {monster.damage}")

            print("1. Attaquer")
            action = input("Votre choix : ")

            if action == "1" or action != "1": 
                damage = max(1, player.attack - monster.defense)
                monster.hp -= damage
                print(f"-> Vous infligez {damage} degats !")
            
            if monster.hp <= 0:
                print(f"Le {monster.name} est vaincu !")
                return True
            
            time.sleep(0.5)
            print(f"\nLe {monster.name} riposte !")
            
            is_dodged = False
            if hasattr(player, 'dodge') and player.dodge > 0:
                if random.randint(1, 100) <= player.dodge:
                    print("SUPERBE ! Vous esquivez l'attaque !")
                    is_dodged = True
            
            if not is_dodged:
                monster_damage = max(1, monster.damage - player.defense)
                player.pv -= monster_damage
                print(f"Vous subissez {monster_damage} degats.")
            
            if player.pv <= 0:
                print("\nVous etes mort...")
                return False

        return False

    def handle_loot(self, player, rank):
        print("\n--- BUTIN ---")
        item = get_loot(rank)
        
        if item:
            print(f"Trouve : {item.name}")
            if hasattr(item, 'damage'):
                print(f"Degats: {item.damage} (Actuel: {player.attack})")
                if input("Equiper ? (o/n) : ") == "o":
                    player.attack = item.damage
                    print("Arme equipee.")
            elif hasattr(item, 'defense'):
                print(f"Defense: {item.defense} (Actuel: {player.defense})")
                if input("Equiper ? (o/n) : ") == "o":
                    player.defense = item.defense
                    print("Armure equipee.")
        else:
            print("Le monstre n'avait rien sur lui.")

def display():
    session = characters()
    session.choice()