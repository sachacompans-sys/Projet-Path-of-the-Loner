import json
import random

class Armor:
    def __init__(self, id: int=0, name: str='none_armor', rarity: str='none_rarity', defense: int = 0):
        self.id = id
        self.name = name
        self.rarity = rarity
        self.defense = defense

    def dice_roll(self, dice_value:int=0):
        print(" ")
        input("Lancer le dé, afin de savoir la rareté de votre armure ->")
        dice_value = random.randint(1,100)
        self.read_Armor(dice_value)


    def read_Armor(self, dice_value:int, rarity_category:str='none-cotegory'):
        with open("armors.json", "r", encoding="utf-8") as f:
            armors_data = json.load(f)
        if 1<= dice_value <= 50 :
            self.rarity = "Common"
            print(f"Vous avez obtenu une armure de rareté : {self.rarity}")
            rarity_category = [item for item in armors_data if item['rarity'] == 'Common']
            
        if 51<= dice_value <= 80:
            self.rarity = "Rare"
            print(f"Vous avez obtenu une armure de rareté : {self.rarity}")
            rarity_category = [item for item in armors_data if item['rarity'] == 'Rare']
            
        if 81<= dice_value <= 95:
            self.rarity = "Epic"
            print(f"Vous avez obtenu une armure de rareté : {self.rarity}")
            rarity_category = [item for item in armors_data if item['rarity'] == 'Epic']
           
        if 96<= dice_value <= 100:
            self.rarity = "Legendary"
            print(f"Vous avez obtenu une armure de rareté : {self.rarity}")
            rarity_category = [item for item in armors_data if item['rarity'] == 'Legendary']

        self.chose_in_rarity(rarity_category)
        
    def chose_in_rarity(self, rarity_category:str):
        display_name = [item['name'] for item in rarity_category]
        print(display_name)
        
    


Test = Armor()
Test.dice_roll()