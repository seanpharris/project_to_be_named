class CharacterTemplate:
    def __init__(self, type, health, attack, defense):
        self.type = type
        self.health = health
        self.attack = attack
        self.defense = defense

Barbarian = CharacterTemplate("Barbarian", 100, 20, 20)

Assasin = CharacterTemplate("Assasin", 60, 40, 10)

Ranger = CharacterTemplate("Ranger", 50, 45, 10)

templates = {
    Barbarian.type: Barbarian,
    Assasin.type: Assasin,
    Ranger.type: Ranger
    }
