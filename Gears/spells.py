class Spells:
    def __init__(self, id: int, name: str, rarity: str, damage: int = 0):
        self.id = id
        self.name = name
        self.rarity = rarity
        self.damage = damage
