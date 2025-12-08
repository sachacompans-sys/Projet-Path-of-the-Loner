import json

merchand_armor = [1,2,3,4,5,6]
merchand_arms = [7,9,10,11,12,13,14]
merchand_potion = [17, 15, 16]
class City_path:

    def __init__(self, user:str,x:int, y:int):
        self.x = x
        self.y = y
        self.user = user

    def current_position(self):
        print(f"Votre {self.user} se trouve aux coordonnée suivantes {self.x};{self.y}")
    
    def Arms_dealer(self):
        self.x += 165
        self.y += 10
        print(f"Vous vous êtes déplacé chez le Marchand d'armes, votre position actuelle est {self.x},{self.y}") 
    
    def Armor_dealer(self):
        self.x = 165
        self.y += 90
        print(f"Vous vous êtes déplacé chez le Marchand d'armures, votre position actuelle est {self.x};{self.y}") 
    
    def Potion_merchant(self):
        self.x -= 665
        self.y -= 10
        print(f"Vous vous êtes déplacé chez le Marchand d'armes, votre position actuelle est {self.x};-{self.y}") 

    def city(self):
        print("Vous voici à Ombreval, la plus grande ville marchande de la région") 
        print("Que vous cherchiez armes, provisions ou informations, vous trouverez tout ici!!")
        player = input("pour rentrer dans ville (1), pour continuer votre chemin (2): ")
        if not player.isnumeric() or player not in ["1", "2"]:
            print("error")
        elif player == "1":
            print("Vous entrez en ville, Partez a la recherche des marchands")   
            player = input("Appuyer sur 3 pour voir les marchands autour: ")
            if not player.isnumeric() or player not in ["3"]:
                print("error")
            elif player == "3":
                print("\n=== MARCHANDS DISPONIBLES ===")
                print("4. Marchand d'armes - Épées, haches, arcs")
                print("5. Marchand d'armures - Casques, plastrons, boucliers")
                print("6. Marchand de potions - Potions de vie, de mana")
                player = input("Pour voir votre postion actuel taper 8: ")
                if player == '8':
                    City = City_path("Hero", 135, 10)
                    City.current_position()
                    print("Pour vous déplacer vers un marchand tapez le numéro qui lui correspond")
                    player = input("Faites votre choix: ")
                    if player not in ["4","5", "6"]:
                        print("error")
                    elif player == "4":
                        City.Arms_dealer()
                        with open("shop.json") as f:
                              data = json.load(f)
                              for item in data:
                                if item["id"] in merchand_arms:
                                    print(json.dumps(item, indent=4, ensure_ascii=False))    
                    elif player == "5":
                        City.Armor_dealer()
                        with open("shop.json") as f:
                              data = json.load(f)
                              for item in data:
                                if item["id"] in merchand_armor:
                                    print(json.dumps(item, indent=4, ensure_ascii=False))    
                    elif player == "6":
                        City.Potion_merchant()
                        with open("shop.json") as f:
                              data = json.load(f)
                              for item in data:
                                if item["id"] in merchand_potion:
                                    print(json.dumps(item, indent=4, ensure_ascii=False))
                else :
                    print("error")
        elif player == "2":
            print("Aurevoir vous vous eloigner de la ville ")
            print("vous avez decider de continuer  votre chemin")
        
City = City_path("Hero", 135, 10)
City.city()
#City.current_position()
#City.move_forward()        