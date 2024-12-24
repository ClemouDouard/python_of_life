class Board:

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        res = ""
        for y in range (self.height):
            res += "| "
            for x in range (self.width):
                res += f"{self.cells[y][x]} | "
            res += "\n"
        return res

    def fill_cells(self) -> None:
        self.cells = [[Cell(x, y, False, self) for x in range(self.width)] for y in range(self.height)]
        for row in self.cells:
            for cell in row:
                cell.calc_neighbors()  # Pré-calcule les voisins

    def set_seed(self, seed: list) -> None:
        for pos in seed:
            self.cells[pos[0]][pos[1]].alive = True

    def next_board(self) -> None:
        next_states = [[cell.set_next() for cell in row] for row in self.cells]
        for y in range (self.height):
            for x in range (self.width):
                self.cells[y][x].alive = next_states[y][x]


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

        if self.alive and (nb_alive < 2 or nb_alive > 3):
            return False
        elif not self.alive and nb_alive == 3:
            return True
        return self.alive
