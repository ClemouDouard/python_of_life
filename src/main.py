from board import Board

if __name__ == "__main__" :
    board = Board(10, 20, [])
    board.fill_cells()

    board.cell(5, 5).calcNeighbors()
    print(board.cell(5, 5).neighbors)
