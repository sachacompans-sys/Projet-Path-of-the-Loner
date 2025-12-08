import json
import random
from time import sleep
import os


class Weapon:
    def __init__(self, id: int=0, name: str='none_weapon', rarity: str='none_rarity', damage: int = 0, bonus: str=''):
        self.id = id
        self.name = name
        self.rarity = rarity
        self.damage = damage
        self.bonus = bonus

    def read_Weapon(self, dice_value: int):
        base_path = os.path.dirname(os.path.dirname(__file__))
        weapon_path = os.path.join(base_path, 'Gears', 'weapons.json')
        
        with open(weapon_path, 'r', encoding='utf-8') as f:
            weapons_data = json.load(f)
        
        if 1 <= dice_value <= 50:
            self.rarity = "Common"
            print()
            sleep(0.5)
            print(f"Vous avez obtenu une arme de rareté : {self.rarity}")
            rarity_category = [item for item in weapons_data if item['rarity'] == 'Common']
            
        elif 51 <= dice_value <= 80:
            self.rarity = "Rare"
            print()
            sleep(0.5)
            print(f"Vous avez obtenu une arme de rareté : {self.rarity}")
            rarity_category = [item for item in weapons_data if item['rarity'] == 'Rare']
            
        elif 81 <= dice_value <= 95:
            self.rarity = "Epic"
            print()
            sleep(0.5)
            print(f"Vous avez obtenu une arme de rareté : {self.rarity}")
            rarity_category = [item for item in weapons_data if item['rarity'] == 'Epic']
           
        elif 96 <= dice_value <= 100:
            self.rarity = "Legendary"
            print()
            sleep(0.5)
            print(f"Vous avez obtenu une arme de rareté : {self.rarity}")
            rarity_category = [item for item in weapons_data if item['rarity'] == 'Legendary']
        
        return rarity_category

    def choice_in_rarity(self, available_weapons, hero_instance):
        if not available_weapons:
            print("Aucune arme trouvée pour cette rareté.")
            return
        
        sleep(1)
        os.system('cls')
        print(f'\nVous pouvez choisir parmi {len(available_weapons)} armes {self.rarity} :\n')
        
        for index, weapon in enumerate(available_weapons, 1):
            bonus_text = f" - Bonus: {weapon['bonus']}" if weapon['bonus'] else ""
            print(f"{index}. {weapon['name']} (Dégâts : {weapon['damage']}){bonus_text}")
        
        print()
        while True:
            try:
                choix_utilisateur = int(input("Votre choix (numéro) : "))
                if 1 <= choix_utilisateur <= len(available_weapons):
                    selected_weapon_data = available_weapons[choix_utilisateur - 1]
                    self.id = selected_weapon_data['id']
                    self.name = selected_weapon_data['name']
                    self.damage = selected_weapon_data['damage']
                    self.bonus = selected_weapon_data.get('bonus', '')
                    print(f"\nVous avez choisi : {self.name}")
                    self.equip_on_hero(hero_instance)
                    break
                else:
                    print(f"Veuillez choisir un nombre entre 1 et {len(available_weapons)}.")
            except ValueError:
                print("Erreur : Veuillez entrer un nombre valide.")

    def equip_on_hero(self, hero):
        hero.attack += self.damage
        print(f"L'arme a été équipée sur {hero.name} !")
        print(f"Son attaque augmente de +{self.damage}.")
        if self.bonus:
            print(f"Bonus spécial : {self.bonus}")
        print(f"Attaque totale : {hero.attack}")


if __name__ == "__main__":
    print("Test Weapon réussi")