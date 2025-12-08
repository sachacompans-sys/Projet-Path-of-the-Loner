import json
import random
import os
from PvE.monsters import Monster

class Room:
    def __init__(self):
        self.monsters = []
        self.load_monsters()

    def load_monsters(self):
        # Trouve le chemin du dossier PvE
        script_folder = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(script_folder, 'bestiary.json')

        try:
            with open(json_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for m in data:
                    # ICI : On utilise les cles exactes de ton JSON (Majuscules)
                    self.monsters.append(Monster(
                        name=m['Name'],
                        hp=m['HP'],
                        damage=m['Damage'],
                        rank=m['Type'],      # Ton JSON dit "Type", mais le code utilise "rank"
                        defense=m['Defense'] # On ajoute la defense
                    ))
        except FileNotFoundError:
            print(f"Erreur : Impossible de trouver bestiary.json dans {script_folder}")
            # Monstre de secours
            self.monsters.append(Monster("Monstre Bug", 50, 5, "Normal", 0))

    def get_normal_room(self):
        normal_monsters = [m for m in self.monsters if m.rank == "Normal"]
        if not normal_monsters: return self.monsters[0]
        return random.choice(normal_monsters)

    def get_elite_room(self):
        elite_monsters = [m for m in self.monsters if m.rank == "Elite"]
        if not elite_monsters: return self.monsters[0]
        return random.choice(elite_monsters)

    def get_boss_room(self):
        boss_monsters = [m for m in self.monsters if m.rank == "Boss"]
        if not boss_monsters: return self.monsters[0]
        return random.choice(boss_monsters)