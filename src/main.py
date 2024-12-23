from board import Board
from config import Settings

if __name__ == "__main__" :
    settings = Settings()
    board = Board(settings.width, settings.height)
    board.fill_cells()
    board.set_seed(settings.seed)

    board.cells[1][4].calc_neighbors()
    for n in board.cells[1][4].neighbors:
        print(n)

    print(board)
    print(board.cells[1][4].set_next())
    print(board)
