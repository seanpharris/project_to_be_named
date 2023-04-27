from objects.weapon import weaponList
from objects.player import player

class CharacterTemplate:
    def __init__(self, type, health, attack, defense, stamina):
        self.type = str(type)
        self.health = int(health)
        self.attack = int(attack)
        self.defense = int(defense)
        self.stamina = str(stamina)
        
# Character templates
Barbarian = CharacterTemplate("Barbarian", 100, 20, 20, 'Low')
Assasin = CharacterTemplate("Assasin", 60, 40, 10, 'High')
Ranger = CharacterTemplate("Ranger", 50, 45, 10, 'Medium')

# Access character templates with dictionary - "templates[<type>.type].<Attribute>"
# Example: templates[Barbarian.type].health
templates = {
    Barbarian.type: Barbarian,
    Assasin.type: Assasin,
    Ranger.type: Ranger
    }

# When building character, use getClassWeapons to build list of weapons for class
def setClassWeapons():
    if player.characterClass == "Barbarian":
        availableWeapons = [
            weaponList['Fist'].name, 
            weaponList['Axe'].name,
            weaponList['Sword'].name
            ]
    elif player.characterClass == "Assasin":
        availableWeapons = [
            weaponList['Fist'].name, 
            weaponList['Poison Dagger'].name,
            weaponList['Bow'].name
            ]
    elif player.characterClass == "Ranger":
        availableWeapons = [
            weaponList['Fist'].name, 
            weaponList['Sword'].name,
            weaponList['Bow'].name
            ]
    return availableWeapons
