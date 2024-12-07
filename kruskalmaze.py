import random
import numpy as np

class MazeGenerator:
    def __init__(self, rows, cols, start, end):
        self.rows = rows
        self.cols = cols
        self.maze = np.ones((rows, cols), dtype=int)  # 1 for walls, 0 for paths
        self.start = start
        self.end = end
        self.parent = {}  # Dictionary to track the parent set of each cell
        self.walls = []   # List of all walls
        self.frames = []  # List to store intermediate states for animation

    def initialize_parents(self):
        for i in range(0, self.rows, 2):
            for j in range(0, self.cols, 2):
                self.parent[(i, j)] = {(i, j)}
        self.parent[tuple(self.start)] = {tuple(self.start)}
        self.parent[tuple(self.end)] = {tuple(self.end)}

    def open_every_other_cell(self):
        for i in range(0, self.rows, 2):
            for j in range(0, self.cols, 2):
                self.maze[i][j] = 0
        self.maze[self.start[0]][self.start[1]] = 0
        self.maze[self.end[0]][self.end[1]] = 0

    def initialize_walls(self):
        for i in range(0, self.rows, 2):
            for j in range(0, self.cols, 2):
                if i + 2 < self.rows:  # Vertical wall
                    self.walls.append(((i, j), (i + 2, j), (i + 1, j)))
                if j + 2 < self.cols:  # Horizontal wall
                    self.walls.append(((i, j), (i, j + 2), (i, j + 1)))
        random.shuffle(self.walls)  # Randomize wall order

    def find_parent(self, cell):
        return self.parent[cell]

    def merge_sets(self, cell1, cell2):
        parent1 = self.find_parent(cell1)
        parent2 = self.find_parent(cell2)

        if parent1 != parent2:  # Only merge disjoint sets
            if len(parent1) > len(parent2):
                larger, smaller = parent1, parent2
            else:
                larger, smaller = parent2, parent1

            for cell in smaller:
                larger.add(cell)
                self.parent[cell] = larger

    def save_frame(self):
        frame = self.maze.copy()
        self.frames.append(frame)

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
