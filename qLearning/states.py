import game_logic.game_constants as gc

def data_prep(game):
    """
    This function is used to prepare the data for the qLearning algorithm.
    It takes a game as input and returns the state of the game.
    """
    state = []
    for i in range(gc.NB_ROWS):
        for j in range(gc.CARDS_PER_ROWS):
            if game.gameboard.rows[i][j] != None:
                state.append([game.gameboard.rows[i][j].value / gc.NB_CARDS])
            else:
                state.append([0])
    for i in range(gc.NB_TURNS):
        if game.player.hand[i] != None:
            state.append([game.player.hand[i].value / gc.NB_CARDS])
        else:
            state.append([0])
    return state