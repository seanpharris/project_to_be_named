import random 

from player import player
from stamina import staminaLevels
from move import moveList, getMoveList
from npc import opponents

###### Round Prep ######
def inputMove(round, moveOptions, chosenMoves):
    try:
        print("Turn %s: " % round)
        # TO DO: Get rid of numerical output for moves
        moveChoice = input()
        print(moveOptions[int(moveChoice)])
        chosenMoves.append(moveOptions[int(moveChoice)])
    except KeyError:
        print("%s is not a move" % (moveChoice))
        inputMove(round, moveOptions, chosenMoves)
    except ValueError:
        print("You did not input a move")
        inputMove(round, moveOptions, chosenMoves)
    return chosenMoves
    
       
def inputRoundMoves(turns, moveOptions):
    chosenMoves = []
    round = 0
    while round != turns:
        round += 1
        chosenMoves = inputMove(round, moveOptions, chosenMoves)
    return chosenMoves
    
def roundPreparation():
    turns = staminaLevels[player.stamina].turns
    staminaExplanation = "Your character has %s stamina. \n" \
                         "This round you have %s moves. \n" \
                            % (player.stamina, turns)
    print(staminaExplanation)
    print("Choose %s moves for this round by selecting the number next to move.\n" 
          % (turns))
    moveOptions = getMoveList(player.weapon)
    # returns list of user input moves
    # access moves as list 
    # example list: chosenMoves = ['Powershot', 'Quickshot', 'Powershot']
    chosenMoves = inputRoundMoves(turns, moveOptions)
    return chosenMoves
###### Round Prep ######

###### Round Combat ######
def getRandomMove(list):
    randomize = random.uniform(0, len(list))
    randomize += 1
    randomMove = list[int(randomize)]
    return randomMove

def getNPCRoundMoves(moveOptions, moveCount):
    npcRoundMoves = []
    for i in range(moveCount):
        randomMove = getRandomMove(moveOptions)
        npcRoundMoves.append(randomMove)
    return npcRoundMoves

def getTheatrics(npcMove, playerMove):
    npcTheatric = moveList[npcMove].theatric
    playerTheatric = moveList[playerMove].theatric
    return npcTheatric, playerTheatric

def calculateDamage(npcMove, npcWeapon, playerMove, playerWeapon):
    npcMoveAttackStat = moveList[npcWeapon][npcMove].attackModifier
    npcMoveDefenseStat = moveList[npcWeapon][npcMove].defenseModifier
    npcMoveCritChance = moveList[npcWeapon][npcMove].critChance

    playerMoveAttackStat = moveList[playerWeapon][playerMove].attackModifier
    playerMoveDefenseStat = moveList[playerWeapon][playerMove].defenseModifier
    playerMoveCritChance = moveList[playerWeapon][playerMove].critChance

    attackStatDiff = npcMoveAttackStat - playerMoveAttackStat
    defenseStatDiff = npcMoveDefenseStat - playerMoveDefenseStat
    

def roundFight(opponentRosterNumber, chosenMoves):
    npcWeapon = opponents[opponentRosterNumber].weapon
    npcStamina = opponents[opponentRosterNumber].stamina
    npcMoveOptions = getMoveList(npcWeapon)
    npcMoveCount = staminaLevels[npcStamina].turns
    npcRoundMoves = getNPCRoundMoves(npcMoveOptions, npcMoveCount)

    playerWeapon = player.weapon
    
    calculateDamage(npcRoundMoves[0], npcWeapon, chosenMoves[0], playerWeapon)
    

chosenMoves = roundPreparation()
roundFight(0, chosenMoves)


