from board import Board

if __name__ == "__main__" :
    board = Board(10, 20)
    board.fill_cells()

    board.cells[5][5].calc_neighbors()
    print(board.cells[5][5].neighbors)

    print(board)
