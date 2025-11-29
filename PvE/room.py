import json
import random
from monsters import Monster


class Room:
    def __init__(self, difficulty : int = 0, monsters : int = []):
        self.difficulty = difficulty
        self.monsters = monsters


    def load_monsters(self):
        with open('PvE/bestiary.json', 'r', encoding='utf-8') as file:
            list_data = json.load(file)

        for monster_dict in list_data:
            new_monster = Monster(monster_dict)
            self.monsters.append(new_monster)


    def generator_difficulty(self):
        Normals = []
        Elites = []
        Boss = []

        for i in self.monsters:
            if i.type == "Normal":
                Normals.append(i)
            elif i.type == "Elite":
                Elites.append(i)    
            elif i.type == "Boss":
                Boss.append(i)

        monster_a = random.choice(Normals)
        monster_b = random.choice(Elites)
        monster_c = random.choice(Boss)

        return {
        "Salle A": monster_a,
        "Salle B": monster_b,
        "Salle C": monster_c
        }