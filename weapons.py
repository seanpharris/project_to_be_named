class Weapon:
    def __init__(self, name, attackModifier, defenseModifier, critChance):
        self.name = str(name)
        self.attackModifier = float(attackModifier)
        self.defenseModifier = float(defenseModifier)
        self.critChance = float(critChance)

# Weapons
fist = Weapon("Fist", .2, .2, 0.01)
sword = Weapon("Sword", .4, .4, 0.2)
axe = Weapon("Axe", .3, .5, 0.1)
bow = Weapon("Bow", .5, .1, 0.3)
poisonDagger = Weapon("Poison Dagger", .5, .2, 0.4)

# Access weapon classes with dictionary - "weaponClass[<weapon>.weapon].<Attribute>"
# Example: weaponClass["Fist"].attackModifier
weaponList = {
    fist.name: fist,
    sword.name: sword, 
    axe.name: axe, 
    bow.name: bow, 
    poisonDagger.name: poisonDagger
    }

# Call function with dictionary index
# Example: getWeaponStats(weapon["Sword"])
def getWeaponStats(weapon):
    stats = "%s stats\n" \
            "Attack modifier: %s\n" \
            "Defense modifier: %s\n" \
            "Crit chance: %s\n" % (weapon.name, weapon.attackModifier,
                                  weapon.defenseModifier, weapon.critChance)
    print(stats)

#getWeaponStats(weaponList["Sword"])
