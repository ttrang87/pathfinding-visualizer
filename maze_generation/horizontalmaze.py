import random
from .share import MazeUtils

class HorizontalMazeGenerator(MazeUtils):
    def __init__(self, rows, cols, start, end):
        super().__init__(rows, cols, start, end)
        # Modify directions to heavily favor vertical movement
        self.directions = [
            (0, 1),   # Down (most frequent)
            (0, -1),  # Up (second most frequent)
            (1, 0),   # Right (less frequent)
            (-1, 0)   # Left (least frequent)
        ]
        # Weights to control direction probability
        self.direction_weights = [0.5, 0.4, 0.05, 0.05]

    def initialize_parents(self):
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.parent[(i, j)] = {(i, j)}

    def generate_maze(self):
        self.open_every_other_cell()
        self.initialize_parents()

        def all_sets_merged():
            unique_parents = set()
            for i in range(0, self.rows, 2):
                for j in range(0, self.cols, 2):
                    unique_parents.add(id(self.find_parent((i, j))))
            return len(unique_parents) == 1  

        while not all_sets_merged():
            x = random.randint(0, self.rows-1)
            y = random.randint(0, self.cols-1)

            if self.maze[x][y] == 0:
                # Use heavily weighted random choice for directions
                dx, dy = random.choices(self.directions, weights=self.direction_weights)[0]
                
                nx, ny = x + dx, y + dy
                cx, cy = nx + dx, ny + dy
                
                if self.is_valid(nx, ny) and self.is_valid(cx, cy) and self.maze[nx][ny] == 1 and self.maze[cx][cy] == 0:
                    cell1 = (x, y)
                    cell2 = (cx, cy)
                    
                    if self.find_parent(cell1) != self.find_parent(cell2):
                        self.maze[nx][ny] = 0  
                        self.merge_sets(cell1, cell2)
                        self.save_frame()

        return self.maze