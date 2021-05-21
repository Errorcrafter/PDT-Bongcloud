def strategy(history,memory):
    
    game_ln = history.shape[1]
    defect_count = 0  # will be saved in memory[0]
    punish_timer = 0  # will be saved on memory[1]
    if memory is None:
        memory = [defect_count,punish_timer]

    if game_ln == 0:  # always comply on the first turn
        choice = 1
    else:
        if history[1,-1] == 1:
            choice = 1