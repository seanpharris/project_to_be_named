class Player:
    def __init__(self, name, characterClass, health, attack, defense, critChance, weapon, stamina):
        self.name = str(name)
        self.characterClass = str(characterClass)
        self.health = int(health)
        self.attack = int(attack)
        self.defense = int(defense)
        self.critChance = float(critChance)
        self.weapon = str(weapon)
        self.stamina = str(stamina)

#player = Player("", "", 0, 0, 0, "", "")

### FOR DEVELOPMENT --- Remove when done
player = Player("Sean", "Ranger", 100, 20, 20, 0, "Bow", "High")
