class Move:
    def __init__(self, name, attackModifier, defenseModifier, critChance, theatric):
        self.name = str(name)
        self.attackModifier = float(attackModifier)
        self.defenseModifier = float(defenseModifier)
        self.critChance = float(critChance)
        self.theatric = str(theatric)
                                   
# Fist
jab = Move("Jab", 0, 0, 0, "POW")
haymaker = Move("Haymaker", 0, 0, 0, "BAM")

fistMoves = { 
    jab.name: jab,
    haymaker.name: haymaker
}

# Axe
verticalSwing = Move("Vertical Swing", 0, 0, 0, "SCHICK")
horizontalSwing = Move("Horizontal Swing", 0, 0, 0, "SCHINK")

axeMoves = { 
    verticalSwing.name: verticalSwing,
    horizontalSwing.name: horizontalSwing
}

# Sword/dagger
hack = Move("Hack", 0, 0, 0, "SCHWACK")
stab = Move("Stab", 0, 0, 0, "SHINK")

bladeMoves = {
    hack.name: hack,
    stab.name: stab
}

# Bow
quickshot = Move("Quickshot", 0, 0, 0, "WIZZZ")
powershot = Move("Powershot", 0, 0, 0, "FLOOP")

bowMoves = {
    quickshot.name: quickshot,
    powershot.name: powershot
}

# Moves shared by all weapons
block = Move("Block", 0, 0, 0, "UGHHH")

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


def getMoveList(weapon):
    moveOptions = {}
    # retrieve weapons for the character's weapon
    allMoves = [move for move in moveList[weapon].keys()]
    # then add the move list shared by all weapons
    [allMoves.append(move) for move in moveList["Shared"].keys()]
    # build a dictionary move list for the character of the combined moves
    for i, move in enumerate(allMoves):
        i += 1
        moveOptions[i]=move
    return moveOptions

# Print all moves for weapon
# print(moveList["Sword"].keys())

