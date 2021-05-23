# SkidV2 by Xianthu (macpherson#1415)

import random

def strategy(history,memory):
    
    game_ln = history.shape[1]
    if memory is None:  # on round start, create vars for memory
        defect_count = 0        # will be saved in memory[0]
        punish_timer = 0        # will be saved in memory[1]
        punish_threshold = 3    # will be saved in memory[2]
        punish_duration = 3     # will be saved in memory[3]
        memory = [defect_count,punish_timer,punish_threshold,punish_duration]
    else:
        defect_count = memory[0]
        punish_timer = memory[1]
        punish_threshold = memory[2]
        punish_duration = memory[3]

    if game_ln == 0:  # always comply on the first turn
        choice = 1
    else:
        punish_timer -= 1  # decrement the timer no matter what

        if history[1,-1] == 1:  # oh look, they are benefiting me!
            #print("a")
            choice = 1
        else:  # hey no fair
            #print("b")
            choice = 1  # forgive them if defect_count is below punish_threshold
            defect_count += 1  # increment

            if defect_count >= punish_threshold and punish_timer < 1:  # start punishing them
                #print("c")
                punish_timer = punish_duration
                choice = 0

            if punish_timer > 1:
                #print("dd")
                choice = 0  # defect go brrrr
            elif punish_timer == 1:
                #print("e")
                choice = 0
                if random.randint(0,1) > 0:  # 1 in 2 chance of becoming angrier
                    punish_duration += 1
                    punish_threshold -= 1
            else:
                pass

    return choice, [defect_count,punish_timer,punish_threshold,punish_duration]
            