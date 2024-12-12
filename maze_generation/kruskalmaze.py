import random
from .share import MazeUtils

class KruskalMazeGenerator(MazeUtils):
    def __init__(self, rows, cols, start, end):
        super().__init__(rows, cols, start, end)
        self.walls = []   # List of all walls

    def initialize_parents(self):
        for i in range(0, self.rows, 2):
            for j in range(0, self.cols, 2):
                self.parent[(i, j)] = {(i, j)}
        self.parent[tuple(self.start)] = {tuple(self.start)}
        self.parent[tuple(self.end)] = {tuple(self.end)}

    def initialize_walls(self):
        for i in range(0, self.rows, 2):
            for j in range(0, self.cols, 2):
                if i + 2 < self.rows:  # Vertical wall
                    self.walls.append(((i, j), (i + 2, j), (i + 1, j)))
                if j + 2 < self.cols:  # Horizontal wall
                    self.walls.append(((i, j), (i, j + 2), (i, j + 1)))
        random.shuffle(self.walls)  # Randomize wall order

    def generate_maze(self):
        self.open_every_other_cell()
        self.initialize_parents()
        self.initialize_walls()

        for cell1, cell2, wall in self.walls:
            if self.find_parent(cell1) != self.find_parent(cell2):

                self.maze[wall] = 0  # Carve the wall (update maze state)
                self.merge_sets(cell1, cell2)
                self.save_frame()


        return self.maze
