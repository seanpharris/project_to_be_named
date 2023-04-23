class Stamina:
    def __init__(self, level, turns, rounds):
        self.level = level
        self.turns = int(turns)
        self.rounds = int(rounds)

# Stamina levels
lowStamina = Stamina("low", 1, 5)
medStamina = Stamina("Medium", 2, 5)
highStamina = Stamina("High", 3, 5)

# Access Stamina with dictionary - "staminaLevels[<level>.level].<Attribute>"
# Example: staminaLevels[lowStamina.level].turns
# Example: staminaLevels["low"].turns
staminaLevels = {
    lowStamina.level: lowStamina,
    medStamina.level: medStamina,
    highStamina: highStamina
}

