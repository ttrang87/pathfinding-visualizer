# models.py
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
