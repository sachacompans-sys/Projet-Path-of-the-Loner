import json
import random
from time import sleep
import os
from ascendency.hero import Hero

class Armor:
    def __init__(self, id: int=0, name: str='none_armor', rarity: str='none_rarity', defense: int = 0):
        self.id = id
        self.name = name
        self.rarity = rarity
        self.defense = defense


    def read_Armor(self, dice_value:int, rarity_category:str):
        with open("armors.json", "r", encoding="utf-8") as f:
                armors_data = json.load(f)

        
        if 1<= dice_value <= 50 :
            self.rarity = "Common"
            print()
            sleep(0.5)
            print(f"Vous avez obtenu une armure de rareté : {self.rarity}")
            rarity_category = [item for item in armors_data if item['rarity'] == 'Common']
            
        elif 51<= dice_value <= 80:
            self.rarity = "Rare"
            print()
            sleep(0.5)
            print(f"Vous avez obtenu une armure de rareté : {self.rarity}")
            rarity_category = [item for item in armors_data if item['rarity'] == 'Rare']
            
        elif 81<= dice_value <= 95:
            self.rarity = "Epic"
            print()
            sleep(0.5)
            print(f"Vous avez obtenu une armure de rareté : {self.rarity}")
            rarity_category = [item for item in armors_data if item['rarity'] == 'Epic']
           
        elif 96<= dice_value <= 100:
            self.rarity = "Legendary"
            print()
            sleep(0.5)
            print(f"Vous avez obtenu une armure de rareté : {self.rarity}")
            rarity_category = [item for item in armors_data if item['rarity'] == 'Legendary']
        
        return rarity_category

        
    def choice_in_rarity(self, rarity_category:str, choice:int=0):
        # count = 0
        # count2 = 0
        # increment = 0
        # display_names = [item['name'] for item in rarity_category]
        # defense_names = [item['defense'] for item in rarity_category]
        # for name in display_names:
        #     count += 1
        # sleep(3)
        # os.system('cls')
        # print()
        # print(f'Vous pouvez choisir {count} armures dans la rareté {self.rarity} :')
        # print()
        # for name in display_names:
        #     count2 +=1
        #     print()
        #     print(f'{name} a {defense_names[increment]} de défense. ({count2})')
        #     increment +=1
        # print()
        # self.choice = input("Votre choix : ")
        # self.add_defense_hero(choice)
        def choice_in_rarity(self, available_armors, hero_instance):
            if not available_armors:
                print("Aucune armure trouvée pour cette rareté.")
                return

            sleep(1) # Raccourci pour le test, remets 3 si tu veux
            # os.system('cls') # Décommenter sur Windows pour nettoyer l'écran

            print(f'\nVous pouvez choisir parmi {len(available_armors)} armures {self.rarity} :')

            # Utilisation de enumerate pour afficher un numéro (1, 2, 3...) devant chaque armure
            # Cela évite de gérer des compteurs manuels
            for index, armor in enumerate(available_armors, 1):
                print(f"{index}. {armor['name']} (Défense : {armor['defense']})")

            print()

            # Boucle pour s'assurer que le joueur entre un bon numéro
            while True:
                try:
                    choix_utilisateur = int(input("Votre choix (numéro) : "))

                    # Vérifie si le numéro est bien dans la liste
                    if 1 <= choix_utilisateur <= len(available_armors):
                        # On récupère l'armure choisie
                        # On fait -1 car les listes commencent à 0, mais l'affichage commence à 1
                        selected_armor_data = available_armors[choix_utilisateur - 1]

                        # Mise à jour des attributs de l'objet Armor actuel
                        self.id = selected_armor_data['id']
                        self.name = selected_armor_data['name']
                        self.defense = selected_armor_data['defense']

                        print(f"\n✅ Vous avez choisi : {self.name}")

                        # APPEL DE LA FONCTION POUR EQUIPER LE HÉROS
                        self.equip_on_hero(hero_instance)
                        break
                    else:
                        print(f"Veuillez choisir un nombre entre 1 et {len(available_armors)}.")
                except ValueError:
                    print("Erreur : Veuillez entrer un nombre valide.")

    def equip_on_hero(self, hero):
        """Met à jour les stats du héros avec l'armure choisie"""
        hero.defense_bonus = self.defense
        print(f"L'armure a été équipée sur {hero.name} !")
        print(f"Sa défense augmente de +{self.defense}.")


# --- ZONE DE TEST (MAIN) ---

if __name__ == "__main__":
    # 1. Création du Héros
    mon_hero = Hero("Lancelot")
    mon_hero.show_stats()

    # 2. Lancement du système d'armure
    systeme_armure = Armor()
    
    # Simulation d'un lancer de dé (ex: 75 pour du Rare)
    valeur_de = random.randint(1, 100)
    
    # Récupération de la liste filtrée
    liste_armures = systeme_armure.get_armors_by_rarity(valeur_de)
    
    # Choix et équipement
    systeme_armure.choice_in_rarity(liste_armures, mon_hero)
    
    # Vérification finale
    mon_hero.show_stats()
        
        
Test = Armor()
Test.read_Armor()
Test.choice_in_rarity()


