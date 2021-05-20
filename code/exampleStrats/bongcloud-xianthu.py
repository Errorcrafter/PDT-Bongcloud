###############################
#                             #
#       BongCloud Strat       #
#  Written by Xianthu Laman   #
#                             #
###############################

import random
import numpy as np

def strategy(history,memory):

    # Declaring variables
    game_length = history.shape[1]
    choice = None

    if game_length > 5: # observe the opponent's actions, choose randomly
        choice = random.randint(0,1)
    else:
        opponent = history[1]

    return choice,memory