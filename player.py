class Player:
    def __init__(self, name, health, attack, defense, combat):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.combat = combat

def getStats():
    stats = "%s's Stats: \n" \
            "   Health:  %s  \n"\
            "   Attack:  %s  \n"\
            "   Defense: %s  \n" % (Player.name, 
                                    Player.health, 
                                    Player.attack, 
                                    Player.defense)
    print(stats)

def getCombat(chosenClass, weaponChoice):
    if chosenClass == 'Barbarian' and weaponChoice == 'Axe':
        Player.combat = weaponChoice
    if chosenClass == 'Barbarian' and weaponChoice == 'Sword':
        Player.combat = weaponChoice
    if chosenClass == 'Barbarian' and weaponChoice == 'Fist':
        Player.combat = weaponChoice
    if chosenClass == 'Assasin' and weaponChoice == 'Fist':
        Player.combat = weaponChoice
    if chosenClass == 'Assasin' and weaponChoice == 'Poison Dagger':
        Player.combat = weaponChoice
    if chosenClass == 'Ranger' and weaponChoice == 'Bow':
        Player.combat = weaponChoice
    if chosenClass == 'Ranger' and weaponChoice == 'Poison Dagger':
        Player.combat = weaponChoice
    else:
        print("%s cannot use that weapon" % (chosenClass))
        getCombat(chosenClass, weaponChoice)
