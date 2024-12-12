import numpy as np

class MazeUtils:
    def __init__(self, rows, cols, start, end):
        self.rows = rows
        self.cols = cols
        self.maze = np.ones((rows, cols), dtype=int)
        self.start = start
        self.end = end
        self.parent = {}
        self.frames = []

    def open_every_other_cell(self):
        for i in range(0, self.rows, 2):
            for j in range(0, self.cols, 2):
                self.maze[i][j] = 0
        self.maze[self.start[0]][self.start[1]] = 0
        self.maze[self.end[0]][self.end[1]] = 0

    def find_parent(self, cell):
        return self.parent[cell]

    def merge_sets(self, cell1, cell2):
        parent1 = self.find_parent(cell1)
        parent2 = self.find_parent(cell2)

        if parent1 != parent2:
            if len(parent1) > len(parent2):
                larger, smaller = parent1, parent2
            else:
                larger, smaller = parent2, parent1

            for cell in smaller:
                larger.add(cell)
                self.parent[cell] = larger
    
    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols

    def save_frame(self):
        frame = self.maze.copy()
        self.frames.append(frame)
