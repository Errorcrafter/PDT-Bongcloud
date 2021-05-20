# SkidStrat by Xianthu
# Bongcloud is horribly broken, so why not make a new one!

import random as r
import numpy as np

def strategy(history,memory):

    if history.shape[1] % 18 == 0: # reset memory every 10 turns
        memory = None

    if memory is None:  # assign a random strat, if none was assigned
        memory = [None,None,None]
        memory[0] = r.choice(["GRIM","TFT","RNG","JOSS","DYNJOSS+","JOSS+"])


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


    elif memory[0] == "RNG":  # Chooses randomly from opponent's moves https://discord.com/channels/844706669455343616/844759135190515762/844887717091344406
        choice = None
        if history.shape[1] == 0:
            choice = 0
        else:
            
            choice = r.choice(history[1])


    elif memory[0] == "JOSS":  # Joss strat from examples
        choice = 1
        if r.random() < 0.10 or (history.shape[1] >= 1 and history[1,-1] == 0):
            choice = 0

    
    elif memory[0] == "DYNJOSS+":  # Joss strat, but more agressive by valadaptive https://github.com/Prisoners-Dilemma-Enjoyers/PrisonersDilemmaTournament/blob/main/code/valadaptive/antijossDynamic.py
        #if threshold is None:
        threshold = 0.1
        choice = 1
        if history.shape[1] >= 1 and history[1, -1] == 0:
            choice = 0
            if r.random() < 0.10:
                choice = 1

        threshold += sum(history[1, -3:]) * 0.0125

    
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