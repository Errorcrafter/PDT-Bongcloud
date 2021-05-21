import random

def strategy(history,memory):
    
    game_ln = history.shape[1]
    if memory is None:  # on round start, create vars for memory
        defect_count = 0        # will be saved in memory[0]
        punish_timer = 0        # will be saved in memory[1]
        punish_threshold = 4    # will be saved in memory[2]
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
            choice = 1
        else:  # hey no fair
            choice = 1  # forgive them if defect_count is below punish_threshold
            defect_count += 1  # increment

            if defect_count == punish_threshold:  # start punishing them
                punish_timer = 3

        if punish_timer > 1:
            choice = 0  # defect go brrrr
        elif punish_timer == 1:
            choice = 0
            if random.random() < 0.20:  # 1 in 5 chance of becoming angrier
                punish_duration += 1
                punish_threshold -= 1

    return choice, memory
            