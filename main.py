import sys
sys.path.append('../game_logic')

import game_logic.game as Game
import display.main as display

if __name__ == "__main__":
    game = Game.Game()
    display.Menu(game)
