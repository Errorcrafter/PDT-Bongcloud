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

def noise(choice,observations): # add additional randomness to screw with people

    try:
        weighting = int(observations) / 7
    except Exception as e:
        return f"ERROR: {str(e)}"
    
    weighting = round(weighting, 3)

    if random.random() > weighting: # if the random number falls abv the weighting.

        if random.randint(1,10) == 1: # flips the choice at random
            choice = not choice

    if random.randint(1,(20*weighting)) == 20*weighting: # very small chance to attempt another flip
        noise(choice,observations)
    else:
        return choice
    

def strategy(history,memory):

    # Declaring variables
    game_length = history.shape[1]
    choice = None

    if game_length > 7: # observe the opponent's actions, choose randomly
        choice = random.randint(0,1)
    else: # after observations
        opponent = history[1]
        obvs = np.count_nonzero(opponent-1)
        if obvs > 5: # low rate of cooperation
            choice = history[1,-1] # Do Tit for Tat
        elif obvs > 3: # middling rate of cooperation
            choice = 1
        else: # very high rate of cooperation, EXPLOIT TIME!!!!!
            choice = 0

    return noise(choice,memory)