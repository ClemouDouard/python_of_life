from board import Board
from config import Settings

class Game:

    def __init__(self, nb_iter: int, settings: Settings) -> None:
        self.board = Board(settings.width, settings.height)
        self.board.fill_cells()
        self.board.set_seed(settings.seed)
        self.nb_iter = nb_iter

    def run(self) -> None:
        for i in range (self.nb_iter):
            print(self.board)
            self.board.next_board()
        print(self.board)
