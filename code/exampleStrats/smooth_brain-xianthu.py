# SmoothBrain by Xianthu (macpherson#1415)


import random


def calc_income(history,rounds):
    game_ln = history.shape[1]
    if game_ln > rounds:
        income = 0
        for i in range(1,rounds):
            if history[0,-i] == 0 and history[1,-1] == 0:  # if both defect
                income += 1
            elif history[0,-i] == 0 and history[1,-1] == 1:  # if you defect
                income += 5
            elif history[0,-i] == 1 and history[1,-1] == 0:  # if opponent defects
                income += 0
            elif history[0,-i] == 1 and history[1,-1] == 1:  # if both comply
                income += 3
            else:
                return "Error!"
    
        return income


def strategy(history,memory):
    
    game_ln = history.shape[1]


    if memory is None:  # on round start, create vars for memory
        defect_count = 0        # will be saved in memory[0]
        punish_timer = 0        # will be saved in memory[1]
        punish_threshold = 3    # will be saved in memory[2]
        punish_duration = 3     # will be saved in memory[3]
        is_punishing = False    # will be saved in memory[4]
        memory = [defect_count,punish_timer,punish_threshold,punish_duration,is_punishing]
    else:
        defect_count = memory[0]
        punish_timer = memory[1]
        punish_threshold = memory[2]
        punish_duration = memory[3]
        is_punishing = memory[4]


    if game_ln == 0:  # always comply on the first turn
        choice = 1
    else:
        punish_timer -= 1  # decrement the timer no matter what

        if history[1,-1] == 1:  # oh look, they are benefiting me!
            choice = 1
        else:  # hey no fair


            choice = 1  # forgive them if defect_count is below punish_threshold
            defect_count += 1  # increment

            if defect_count >= punish_threshold and punish_timer < 1:  # start punishing them when too many defects
                punish_timer = punish_duration
                is_punishing = True  # makes use of le punish timer
                choice = 0


            if game_ln> 10:
                if calc_income(history,10) <= 10:  # always punish if opponent has defaulted to always defect
                    is_punishing = True
                    punish_timer = 999999999


        if is_punishing == True:

            if punish_timer > 1:
                choice = 0  # defect go brrrr

            elif punish_timer == 1:  # when defect timer stops

                choice = 0
                is_punishing = False
                if random.randint(1,4) != 4:  # 3 in 4 chance of becoming angrier :troll:
                    punish_duration += 1
                    punish_threshold -= 1
                defect_count = 0
            else:
                pass


    return choice, [defect_count,punish_timer,punish_threshold,punish_duration,is_punishing]
            