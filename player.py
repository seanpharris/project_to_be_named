class Player:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

def getStats():
    stats = "%s's Stats: \n" \
            "   Health:  %s  \n"\
            "   Attack:  %s  \n"\
            "   Defense: %s  \n" % (Player.name, 
                                    Player.health, 
                                    Player.attack, 
                                    Player.defense)
    print(stats)
