class Combat:
    def __init__(self, weapon, attack_modifier, defense_modifier):
        self.weapon = weapon
        self.attack_modifier = attack_modifier
        self.defense_modifier = defense_modifier

fistFighter = Combat("Fist", .2, .2)

swordFighter = Combat("Sword", .4, .4)

axeFighter = Combat("Axe", .3, .5)

bowFighter = Combat("Bow", .5, .1)

poisonDaggerFighter = Combat("Poison Dagger", .5, .2)

combatOptions = {
    fistFighter.weapon: fistFighter,
    swordFighter.weapon: swordFighter, 
    axeFighter.weapon: axeFighter, 
    bowFighter.weapon: bowFighter, 
    poisonDaggerFighter.weapon: poisonDaggerFighter
    }


