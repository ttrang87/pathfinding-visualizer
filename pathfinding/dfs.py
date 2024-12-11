class Depth_First_Search:
    def __init__(self, maze):
        self.maze = maze

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


    
    