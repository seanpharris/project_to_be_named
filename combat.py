import random 

from player import player
from stamina import staminaLevels
from move import moveList, getMoveList, getMoveStats
from npc import opponents, getNPCRoundMoves
from characterUtilities import getTheatric, modifyStats

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
    print(moveOptions)
    # returns list of user input moves
    # access moves as list 
    # example list: chosenMoves = ['Powershot', 'Quickshot', 'Powershot']
    chosenMoves = inputRoundMoves(turns, moveOptions)
    print("___________________________")
    print("______Moves Selected_______")
    print("___________________________\n")
    return chosenMoves
###### Round Prep ######

###### Round Combat ######

# Determine how many rounds there will be based off which character has
# more stamina/moves and add the exhasuted move if one has less
def getNumberOfTotalTurns(npcRoundMoves):
    totalRounds = 0
    exhausted = moveList['Shared']['Exhausted'].name
    if len(npcRoundMoves) > len(chosenPlayerMoves):
        chosenPlayerMoves.append(exhausted)
        totalRounds = len(npcRoundMoves)
    elif len(npcRoundMoves) < len(chosenPlayerMoves):
        npcRoundMoves.append(exhausted)
        totalRounds = len(chosenPlayerMoves)
    else:
        totalRounds = len(chosenPlayerMoves)
    return totalRounds

#def calculateDamage():


def roundFight(opponentRosterNumber, chosenPlayerMoves):
    opponent = opponents[opponentRosterNumber]
    npcMoveOptions = getMoveList(opponent.weapon)
    npcMoveCount = staminaLevels[opponent.stamina].turns
    npcRoundMoves = getNPCRoundMoves(npcMoveOptions, npcMoveCount)
    
    totalTurns = getNumberOfTotalTurns(npcRoundMoves)
    # Move used as an integer to index the moves list for player/npc
    for turn in range(totalTurns):
        # Theatrics!
        npcTheatric = getTheatric(opponent.weapon, npcRoundMoves[turn])
        playerTheatric = getTheatric(player.weapon, chosenPlayerMoves[turn])
        print("Round Fight! " + npcTheatric + " " + playerTheatric)
        # Stats!
        npcMoveStats = getMoveStats(npcRoundMoves[turn], opponent.weapon)
        playerMoveStats = getMoveStats(chosenPlayerMoves[turn], player.weapon)
        
        characterStats = ["attack", "defense", "critChance"]
        modifyStats(opponent, characterStats, npcMoveStats)
        modifyStats(player, characterStats, playerMoveStats)

        #calculateDamage()
    

chosenPlayerMoves = roundPreparation()
roundFight(0, chosenPlayerMoves)


