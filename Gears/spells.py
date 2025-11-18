class Spell:
    def __init__(self, mana_cost=float, name=str, damage=float):
        self.mana_cost = mana_cost
        self.name = name
        self.damage = damage