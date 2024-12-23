from game import Game
from config import Settings

if __name__ == "__main__" :
    settings = Settings()
    game = Game(10, settings)

    game.run()
