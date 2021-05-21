# SkidStrat by Xianthu (macpherson#1415)
# Bongcloud is horribly broken, so why not make a new one!
# Unholy abomination of a bunch of well-performing strats.
# Creds to the CaryKH's Prisoner Dilemma Project Discord server where I skidded most of this from 😎😎😎

import random as r
import numpy as np

def strategy(history,memory):

    game_ln = history.shape[1]

    if game_ln % 20 == 0: # resets memory to use a new strat
        memory = None

    if memory is None:  # assign a random strat, if none was assigned
        memory = [None,  # stores strat name (0)
                  None,  # grim's memory     (1)
                  None]  # gmtft's memory    (2)
        memory[0] = r.choice(["GRIM","GTFT","RNG","JOSS","DYNJOSS+","JOSS+","BAL"])


    if memory[0] == "GRIM":  # GrimTrigger strat in examples.
        wronged = False
        if memory[1] is not None and memory[1]: # Has memory that it was already wronged.
            wronged = True
        else: # Has not been wronged yet, historically.
            if game_ln >= 1 and history[1,-1] == 0: # Just got wronged.
                wronged = True
        
        if wronged:
            #return 0, True
            choice = 0
            memory[1] = True # grim's memory is stored in memory[1]
        else:
            #return 1, False
            choice = 1
            memory[1] = False


    elif memory[0] == "GTFT":  # Relaxed Grim Moral TFT by EFHIII(?) https://github.com/Prisoners-Dilemma-Enjoyers/PrisonersDilemmaTournament/blob/main/code/misc/relaxedGrimMoralTitForTat.py
        if memory[2] is not None and memory[2][0] is True:
            remainingPunishments = memory[1] - 1
            punishMode = remainingPunishments > 0
            return 0, (punishMode, remainingPunishments)

        if memory[2] is not None and memory[2][1] >= 5:
            return 0, (True, 4)

        #num_rounds = game_ln
        opponents_last_move = history[1, -1] if game_ln >= 1 else 1
        opponents_second_last_move = history[1, -2] if game_ln >= 2 else 1
        our_second_last_move = history[0, -2] if game_ln >= 2 else 1
        choice = (
            1
            if (
                opponents_last_move == 1
                or (our_second_last_move == 0 and opponents_second_last_move == 1)
            )
            else 0
        )
        if choice == 0:
            memory[2] = (False, 1) if memory[2] is None else (False, memory[2][1] + 1)

        #return choice, memory


    elif memory[0] == "RNG":  # Chooses randomly from opponent's moves https://discord.com/channels/844706669455343616/844759135190515762/844887717091344406
        choice = None
        if game_ln == 0:
            choice = 0
        else:
            
            choice = r.choice(history[1])


    elif memory[0] == "JOSS":  # Joss strat from examples
        choice = 1
        if r.random() < 0.10 or (game_ln >= 1 and history[1,-1] == 0):
            choice = 0

    
    elif memory[0] == "DYNJOSS+":  # Joss strat, but more agressive by valadaptive https://github.com/Prisoners-Dilemma-Enjoyers/PrisonersDilemmaTournament/blob/main/code/valadaptive/antijossDynamic.py
        #if threshold is None:
        threshold = 0.1
        choice = 1
        if game_ln >= 1 and history[1, -1] == 0:
            choice = 0
            if r.random() < 0.10:
                choice = 1

        threshold += sum(history[1, -3:]) * 0.0125

    
    elif memory[0] == "JOSS+":  # AntiAntiJoss by nekiwo https://github.com/Prisoners-Dilemma-Enjoyers/PrisonersDilemmaTournament/blob/main/code/nekiwo/antiAntiJoss.py
        choice = 1
        if game_ln >= 1 and history[1, -1] == 0:
            choice = 0
            if r.random() < 0.10:
                choice = 1
                if r.random() < 0.10:
                    choice = 0


    elif memory[0] == "BAL":  # Balance by Saffron https://github.com/Prisoners-Dilemma-Enjoyers/PrisonersDilemmaTournament/blob/main/code/saffron/balance.py
        choice = 1
        if game_ln != 0:
            percents = np.mean(history, axis=1)
            if percents[0] > percents[1] + 0.1:
                choice = 0


    else:  # if the code does le epic crew up just defect
        choice = 0


    if game_ln > 4:  # checks the prev 4 moves to see if its been doing the same thing for a long time
        if history[1,-4] == history[1,-3] == history[1,-2] == history[1,-1]:
            choice = 0  # defect just in case


    
    return choice,memory