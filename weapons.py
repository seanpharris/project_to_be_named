class Weapon:
    def __init__(self, weapon, attackModifier, defenseModifier):
        self.weapon = weapon
        self.attackModifier = attackModifier
        self.defenseModifier = defenseModifier

# Weapon classes
fistFighter = Weapon("Fist", .2, .2)
swordFighter = Weapon("Sword", .4, .4)
axeFighter = Weapon("Axe", .3, .5)
bowFighter = Weapon("Bow", .5, .1)
poisonDaggerFighter = Weapon("Poison Dagger", .5, .2)

# Access weapon classes with dictionary - "weaponClass[<weapon>.weapon].<Attribute>"
# Example: weaponClass["Fist"].attackModifier
weaponClass = {
    fistFighter.weapon: fistFighter,
    swordFighter.weapon: swordFighter, 
    axeFighter.weapon: axeFighter, 
    bowFighter.weapon: bowFighter, 
    poisonDaggerFighter.weapon: poisonDaggerFighter
    }

moveList = {
    "Jab": , 
    "Haymaker": , 
    "Block":
    "Vertical Swing": , 
    "Horizontal Swing": , 
    "Block": ,
    "Stab", 
    "Hack", 
    "Block"
    "Quickshot", 
    "Powershot", 
    "Block"
}
