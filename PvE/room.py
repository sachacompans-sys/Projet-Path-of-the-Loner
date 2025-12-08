import json
import random
from monsters import Monster

class Room:
    def __init__(self):
        self.normals = []
        self.elites = []
        self.bosses = []
        self.load_monsters()

    def load_monsters(self):
        with open('bestiary.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        for monster_dict in data:
            mob = Monster(monster_dict)
            
            if mob.type == "Normal":
                self.normals.append(mob)
            elif mob.type == "Elite":
                self.elites.append(mob)
            elif mob.type == "Boss":
                self.bosses.append(mob)

    def get_normal_room(self):
        print("--- Vous entrez dans une salle sombre et humide... ---")
        mob = random.choice(self.normals)
        print(f" {mob.name} | (HP: {mob.hp} | Dégâts: {mob.damage} | Défense: {mob.defense}) surgit de l'ombre pour attaquer !")
        return mob

    def get_elite_room(self):
        print("--- L'air devient lourd, une menace puissante approche... ---")
        mob = random.choice(self.elites)
        print(f"ATTENTION : {mob.name} | (HP: {mob.hp} | Dégâts: {mob.damage} | Défense: {mob.defense}) vous barre la route !")
        return mob

    def get_boss_room(self):
        print("--- VOUS SENTEZ UNE PRÉSENCE TERRIFIANTE... ---")
        mob = random.choice(self.bosses)
        print(f"DANGER MORTEL : {mob.name} | (HP: {mob.hp} | Dégâts: {mob.damage} | Défense: {mob.defense}) est devant vous !!")
        return mob