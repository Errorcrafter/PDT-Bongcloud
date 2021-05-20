###############################
#                             #
#       Bongcloud Strat       #
#  Written by Xianthu Laman   #
#                             #
###############################

# defect      > 0
# cooperate   > 1

import random
import numpy as np

def noise(choice,observations:int): # add additional randomness to screw with people

    try:
        weighting = int(observations) / 7
    except Exception as e:
        return f"ERROR: {str(e)}"
    
    weighting = round(weighting, 3)

    if random.random() > weighting: # if the random number falls abv the weighting.

        if random.randint(1,10) == 1: # flips the choice at random
            choice = not choice

    if random.randint(1,200) == 200: # very small chance to attempt another flip
        noise(choice,observations)
    else:
        return choice
    

def strategy(history,memory):

    # Declaring variables
    game_length = history.shape[1]
    choice = None
    obvs = None

    if game_length > 7: # observe the opponent's actions, choose randomly
        choice = random.randint(0,1)

    elif game_length > 20: # after observations, phase 1 - pseudo-random (prolly broken)
        opponent = history[1]
        obvs = np.count_nonzero(opponent-1)
        if obvs > 5: # low rate of cooperation
            choice = history[1,-1] # Do Tit for Tat
        elif obvs > 3: # middling rate of cooperation
            choice = 0
        else: # very high rate of cooperation, EXPLOIT TIME!!!!!
            choice = 0

    elif game_length > 40: # phase 2 - grimTrigger?
        pass

    else: # final phase - always defect
        pass

    return noise(choice,obvs),memory