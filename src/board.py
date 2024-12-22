class Board:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.cells = [[Cell for _ in range(width)] for _ in range(height)]

    def fill_cells(self) -> None:
        for i in range (self.height) :
            for j in range (self.width) :
                self.cells[i][j] = Cell(j, i, False, self)

    def get_cells(self) -> list:
        return self.cells

class Cell:

    def __init__(self, x: int, y: int, alive: bool, b: Board) -> None:
        self.x = x
        self.y = y
        self.alive = alive
        self.board = Board

    def calc_neighbors(self) -> None:
            self.neighbors = []
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue

                    nx, ny = self.x + dx, self.y + dy

                    # verify if in limit
                    if 0 <= nx < self.board.width and 0 <= ny < self.board.height:
                        neighbor = self.board.get_cells()[ny][nx]
                        self.neighbors.append(neighbor)
