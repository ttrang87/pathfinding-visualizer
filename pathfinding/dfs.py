class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def up(self):
        return Cell(self.x - 1, self.y)  

    def down(self):
        return Cell(self.x + 1, self.y)  

    def left(self):
        return Cell(self.x, self.y - 1)  

    def right(self):
        return Cell(self.x, self.y + 1)  
    
class Maze:
    def __init__(self, maze):
        self.maze = maze  
        self.rows = len(maze)
        self.cols = len(maze[0])

    def is_valid(self, cell, start, end):
        if start and (cell.x == start.x and cell.y == start.y):
            return True
        if end and (cell.x == end.x and cell.y == end.y):
            return True
        return 0 <= cell.x < self.rows and 0 <= cell.y < self.cols and self.maze[cell.x][cell.y] == 0


class Depth_First_Search:
    def __init__(self, maze):
        self.maze = maze
        self.visited = set()  
        self.path = [] 
        self.visited_cells = [] #use for animation (each step)

    def search(self, start, end):
        self.visited = set()
        self.path = []
        self.visited_cells = []
        self.dfs(start, start, end)  
        if not self.path:
            return None
        return self.path, self.visited_cells

    def dfs(self, current, start, end):
        if current.x == end.x and current.y == end.y:
            self.path.append((current.x, current.y))  
            return True

        self.visited.add((current.x, current.y))
        self.visited_cells.append((current.x, current.y))

        for direction in ['up', 'right', 'down', 'left']:
            next_cell = getattr(current, direction)()  
            if ((next_cell.x, next_cell.y) not in self.visited and self.maze.is_valid(next_cell, start, end)):
                if self.dfs(next_cell, start, end):
                    self.path.append((current.x, current.y))  
                    return True

        return False


    
    