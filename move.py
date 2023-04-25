class Move:
    def __init__(self, name, attackModifier, defenseModifier, critChance):
        self.name = str(name)
        self.attackModifier = float(attackModifier)
        self.defenseModifier = float(defenseModifier)
        self.critChance = float(critChance)
                                   
# Fist
jab = Move("Jab", 0, 0, 0)
haymaker = Move("Haymaker", 0, 0, 0)

fistMoves = { 
    jab.name: jab,
    haymaker.name: haymaker
}

# Axe
verticalSwing = Move("Vertical Swing", 0, 0, 0)
horizontalSwing = Move("Horizontal Swing", 0, 0, 0)

axeMoves = { 
    verticalSwing.name: verticalSwing,
    horizontalSwing.name: horizontalSwing
}

# Sword/dagger
hack = Move("Hack", 0, 0, 0)
stab = Move("Stab", 0, 0, 0)

bladeMoves = {
    hack.name: hack,
    stab.name: stab
}

# Bow
quickshot = Move("Quickshot", 0, 0, 0)
powershot = Move("Powershot", 0, 0, 0)

bowMoves = {
    quickshot.name: quickshot,
    powershot.name: powershot
}

# Moves shared by all weapons
block = Move("Block", 0, 0, 0)

sharedMoves = {
    block.name: block
}

# Access Moves with dictionary - "moveList[<weapon>][<move>].<Attribute>"
# Example: moveList["Sword"]["Hack"].critChance
moveList = {
    "Fist": fistMoves,
    "Axe": axeMoves,
    "Sword" or "Dagger": bladeMoves,
    "Bow": bowMoves,
    "Shared": sharedMoves
}

# Call function with dictionary index
# Example: getMoveStats(moveList["Sword"]["Hack"])
def getMoveStats(weaponMove):
    stats = "%s stats\n" \
            "Attack modifier: %s\n" \
            "Defense modifier: %s\n" \
            "Crit chance: %s\n" % (weaponMove.name, weaponMove.attackModifier,
                                  weaponMove.defenseModifier, weaponMove.critChance)
    print(stats)

# Print all moves for weapon
# print(moveList["Sword"].keys())

