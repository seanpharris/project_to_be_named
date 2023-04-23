from weapons import weaponClass
from player import player

class CharacterTemplate:
    def __init__(self, type, health, attack, defense, stamina):
        self.type = type
        self.health = health
        self.attack = attack
        self.defense = defense
        self.stamina = stamina
        
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
def getClassWeapons():
    if player.characterClass == "Barbarian":
        availableWeapons = [
            weaponClass['Fist'].weapon, 
            weaponClass['Axe'].weapon,
            weaponClass['Sword'].weapon
            ]
    elif player.characterClass == "Assasin":
        availableWeapons = [
            weaponClass['Fist'].weapon, 
            weaponClass['Poison Dagger'].weapon,
            weaponClass['Bow'].weapon
            ]
    elif player.characterClass == "Ranger":
        availableWeapons = [
            weaponClass['Fist'].weapon, 
            weaponClass['Sword'].weapon,
            weaponClass['Bow'].weapon
            ]
    return availableWeapons
