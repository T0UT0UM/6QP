import sys
sys.path.append('../game_logic')
sys.path.append('../display')

from game_logic.game import Game
import display.main as display

if __name__ == "__main__":
    game = Game()
    display.Menu(game)
