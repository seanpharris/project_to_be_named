class Stamina:
    def __init__(self, level, turns, rounds):
        self.level = str(level)
        self.turns = int(turns)
        self.rounds = int(rounds)

# Stamina levels
lowStamina = Stamina("Low", 1, 5)
medStamina = Stamina("Medium", 2, 5)
highStamina = Stamina("High", 3, 5)

# Access Stamina with dictionary - "staminaLevels[<level>.level].<Attribute>"
# Example: staminaLevels[lowStamina.level].turns
# Example: staminaLevels["Low"].turns
staminaLevels = {
    lowStamina.level: lowStamina,
    medStamina.level: medStamina,
    highStamina.level: highStamina
}

