import random
from .share import MazeUtils

class RandomMazeGenerator(MazeUtils):
    def __init__(self, rows, cols, start, end):
        super().__init__(rows, cols, start, end)
        self.count_cells = rows * cols // 4.5
    
    def initialize_parents(self):
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.parent[(i, j)] = {(i, j)}

    def generate_maze(self):
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.maze[i][j] = 0

        count = 0

        while count < self.count_cells:
            x = random.randint(0, self.rows-1)
            y = random.randint(0, self.cols-1)
            if self.is_valid(x,y) and self.maze[x][y]  == 0:
                self.maze[x][y] = 1
                count += 1
                self.save_frame()

        return self.maze