Path of the Loner
Bienvenue sur Path of the Loner, un jeu de rôle (RPG) textuel développé en Python. Ce projet est construit autour des principes de la Programmation Orientée Objet (POO) pour gérer les entités, les équipements et les interactions.

📋 Description
Ce jeu permet d'incarner un héros, de s'équiper, de combattre des monstres et de progresser à travers différents environnements. L'architecture sépare clairement la logique du jeu (classes Python) des données (fichiers JSON).

📂 Structure du Projet
L'organisation des fichiers est pensée par modules fonctionnels :

1. 🧙‍♂️ Ascendency (Le Héros)
Gestion de la création et de l'évolution du personnage.

Hero : La classe principale du joueur.

Ancestry : Gestion des origines/classes (données stockées dans Ancestry.json).

2. ⚔️ Gears (Équipement)
Tout ce qui concerne l'inventaire et les statistiques de combat.

Weapons / Armor / Spells : Classes gérant les objets.

Fichiers JSON : (Weapons.json, Armor.json, Spells.json) contiennent les statistiques et descriptions des objets.

3. 🗺️ PvE (Aventure)
Le cœur du gameplay "Player vs Environment".

Rooms / Monsters : Génération des lieux et des ennemis (Bestiary.json).

Merchants / Loot : Gestion de l'économie (Shop.json) et des récompenses.

4. 🖥️ Menu (Interface)
display : Gestion de l'affichage console.

PvP : (Optionnel/En développement) Module pour le "Player vs Player".