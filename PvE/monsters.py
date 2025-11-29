class Monster:
    def __init__(self, data):
        self.name = data["Name"]
        self.type = data["Type"]
        self.hp = data["HP"]
        self.damage = data["Damage"]
        self.defense = data["Defense"]
        self.gold = data["gold_drop"]