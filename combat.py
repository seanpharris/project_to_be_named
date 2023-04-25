from player import player
from stamina import staminaLevels
from move import moveList

def getMoves(turns, moveOptions):
    chosenMoves = []
    remaingTurns = turns
    ## CURRENT PROBLEM:
    ## Trying to get turn to be the correct number after failing to input 
    ## a real move number
    ## Turn starts over after inputting a non real move number
    try:
        for turn in range(remaingTurns):
            remaingTurns -= 1
            turn += 1
            moveChoice = input("Turn %s: " % turn)
            print(moveOptions[int(moveChoice)])
            chosenMoves.append(moveOptions[int(moveChoice)])
    except KeyError:
        print("%s is not a move" % (moveChoice))
    ## The culprit is "turn" in line 22
        getMoves(turn, moveOptions)
    

def roundPreparation():
        turns = staminaLevels[player.stamina].turns
        staminaExplanation = "Your character has %s stamina. \n" \
                             "This round you have %s moves. \n" \
                                % (player.stamina, turns)
        print(staminaExplanation)

        print("Choose %s moves for this round by selecting the number next to move.\n" 
              % (turns))

        # List of all moves for the players weapon then append all the shared moves
        allMoves = [move for move in moveList[player.weapon].keys()]
        [allMoves.append(move) for move in moveList["Shared"].keys()]

        moveOptions = {}
        for i, move in enumerate(allMoves):
                i += 1
                moveOptions[i]=move
                print("(%s) %s \n" % (i, move))
        
        
        getMoves(turns, moveOptions)

        
roundPreparation()


