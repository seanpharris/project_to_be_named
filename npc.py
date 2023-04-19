class NPC:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

# TO DO: Make more NPCs and add to oppenents list
Henchman = NPC("Henchman", 70, 10, 10)

oppenents = [Henchman]
