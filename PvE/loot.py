import json
import random
import os
from Gears.weapons import Weapon
from Gears.armor import Armor

def get_loot(monster_rank):
    try:
        with open('Gears/weapons.json', 'r', encoding='utf-8') as file:
            data_weapon = json.load(file)

        with open('Gears/armor.json', 'r', encoding='utf-8') as file:
            data_armor = json.load(file)
    except FileNotFoundError:
        print("Erreur : Fichiers JSON introuvables.")
        return None

    all_items = []
    for weapon in data_weapon:
        weapon['item_type'] = 'weapon'
        all_items.append(weapon)
    
    for armor in data_armor:
        armor['item_type'] = 'armor'
        all_items.append(armor)

    loot_pool = []

    if monster_rank == "Normal":
        loot_pool = [i for i in all_items if i['rarity'] == "Common"]
        if random.random() < 0.15:
            #Le .extend sert Ã virer si l'utilisateur drop un rare au lieu d'un commun
            loot_pool.extend([i for i in all_items if i['rarity'] == "Rare"])

    elif monster_rank == "Elite":
        loot_pool = [i for i in all_items if i['rarity'] in ["Rare", "Epic"]]

    elif monster_rank == "Boss":
        loot_pool = [i for i in all_items if i['rarity'] in ["Epic", "Legendary"]]


    drop_chance = 70 
    roll = random.randint(1, 100)

    if roll <= drop_chance:
        # On pioche dans la Loot Pool une armure ou une arme
        selected_data = random.choice(loot_pool)
        
        final_loot = None

        if selected_data['item_type'] == 'weapon':
            final_loot = Weapon(
                id=selected_data['id'],
                name=selected_data['name'],
                damage=selected_data['damage'],
                rarity=selected_data['rarity']
            )
        else:
            final_loot = Armor(
                id=selected_data['id'],
                name=selected_data['name'],
                defense=selected_data['defense'],
                rarity=selected_data['rarity']
            )
        print(f"Vous avez obtenu : {final_loot.name}, {final_loot.rarity}")
        
        return final_loot

    else:
        return None