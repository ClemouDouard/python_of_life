class Board:

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        res = ""
        for x in range (self.height):
            res += "| "
            for y in range (self.width):
                res += f"{self.cells[x][y]} | "
            res += "\n"
        return res

    def fill_cells(self) -> None:
        self.cells = []
        for i in range (self.height) :
            self.cells.append([])
            for j in range (self.width) :
                self.cells[i].append(Cell(j, i, False, self))

    def set_seed(self, seed: list) -> None:
        for pos in seed:
            self.cells[pos[0]][pos[1]] = Cell(pos[0], pos[1], True, self)

class Cell:

    def __init__(self, x: int, y: int, alive: bool, b: Board) -> None:
        self.x = x
        self.y = y
        self.alive = alive
        self.board = b

    def __str__(self) -> str:
        if self.alive == True:
            return "1"
        else:
            return "0"

    def calc_neighbors(self) -> None:
        self.neighbors = []
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
               if dx == 0 and dy == 0:
                   continue

               nx, ny = self.x + dx, self.y + dy

               # verify if in limit
               if 0 <= nx < self.board.width and 0 <= ny < self.board.height:
                    neighbor = self.board.cells[ny][nx]
                    self.neighbors.append(neighbor)

    def set_next(self) -> bool:
        nb_alive = 0

        for neighbor in self.neighbors:
            if neighbor.alive == True:
                nb_alive+=1

        if self.alive == True and 2 > nb_alive < 3:
            self.alive = False
            return False
        elif self.alive == False and nb_alive == 3:
            self.alive = True
            return True

        return self.alive
