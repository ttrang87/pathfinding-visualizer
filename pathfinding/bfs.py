from collections import deque

class Breadth_First_Search:
    def __init__(self, maze):
        self.maze = maze

    def search(self, start, end):
        self.visited = set()
        self.visited_cells = []

        queue = deque([(start, [start])])

        while queue:
            current, path = queue.popleft()
            self.visited.add((current.x, current.y))
            self.visited_cells.append((current.x, current.y))

            if current.x == end.x and current.y == end.y:
                return [(cell.x, cell.y) for cell in path], self.visited_cells

            for direction in ['up', 'down', 'left', 'right']:
                next_cell = getattr(current, direction)()
                if (next_cell.x, next_cell.y) not in self.visited and self.maze.is_valid(next_cell, start, end):
                    self.visited.add((next_cell.x, next_cell.y))
                    queue.append((next_cell, path + [next_cell]))

        return None, self.visited_cells

    
