# Split Personality by Xianthu
# Bongcloud is horribly broken, so why not make a new one!

import random as r
import numpy as np

def strategy(history,memory):

    if history.shape[1] % 10 == 0: # reset memory every 10 turns
        memory = None

    if memory is None:  # assign a random strat, if none was assigned
        memory = [None,None,None]
        memory[0] = r.choice(["GRIM","TFT","DETECT","RNG","JOSS","AGGRO_JOSS","JOSS+"])


    if memory[0] == "GRIM":  # GrimTrigger strat in examples.
        wronged = False
        if memory[1] is not None and memory[1]: # Has memory that it was already wronged.
            wronged = True
        else: # Has not been wronged yet, historically.
            if history.shape[1] >= 1 and history[1,-1] == 0: # Just got wronged.
                wronged = True
        
        if wronged:
            #return 0, True
            choice = 0
            memory[1] = True # grim's memory is stored in memory[1]
        else:
            #return 1, False
            choice = 1
            memory[1] = False


    elif memory[0] == "TFT":  # Forgiving Tit For Tat strat from examples
        choice = 1
        if history.shape[1] >= 2 and history[1,-1] == 0 and history[1,-2] == 0: # forgiving tft go brrrrrrrr
            choice = 0


    elif memory[0] == "DETECT":  # Detective strat from examples
        testingSchedule = [1,0,1,1]
        gameLength = history.shape[1]
        shallIExploit = memory[2] # detective's memory is stored in memory[2]
        choice = None
        
        if gameLength < 4: # We're still in that initial testing stage.
            choice = testingSchedule[gameLength]
        elif gameLength == 4: # Time to analyze the testing stage and decide what to do based on what the opponent did in that time!
            opponentsActions = history[1]
            if np.count_nonzero(opponentsActions-1) == 0: # The opponent cooperated all 4 turns! Never defected!
                shallIExploit = True # Let's exploit forever.
            else:
                shallIExploit = False # Let's switch to Tit For Tat.
        
        if gameLength >= 4:
            if shallIExploit:
                choice = 0
            else:
                choice = history[1,-1] # Do Tit for Tat
        
        #return choice, shallIExploit
        memory[2] = shallIExploit


    elif memory[0] == "RNG":  # Random
        choice = r.choice([0,1])


    elif memory[0] == "JOSS":  # Joss strat from examples
        choice = 1
        if r.random() < 0.10 or (history.shape[1] >= 1 and history[1,-1] == 0):
            choice = 0

    
    elif memory[0] == "AGGRO_JOSS":  # Joss strat, but more agressive
        choice = 1
        if r.random() < 0.30 or (history.shape[1] >= 1 and history[1,-1] == 0):
            choice = 0

    
    elif memory[0] == "JOSS+":  # AntiAntiJoss by nekiwo https://github.com/Prisoners-Dilemma-Enjoyers/PrisonersDilemmaTournament/blob/main/code/nekiwo/antiAntiJoss.py
        choice = 1
        if history.shape[1] >= 1 and history[1, -1] == 0:
            choice = 0
            if r.random() < 0.10:
                choice = 1
                if r.random() < 0.10:
                    choice = 0


    else:
        choice = 0

    
    return choice,memory