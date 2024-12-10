import heapq

class A_Star:
    def __init__(self, maze):
        self.maze = maze
        self.visited_cells = []  # For animation 
    
    def search(self, start, end):
        def heuristic(point):
        # Manhattan distance heuristic
            return abs(point[0] - end[0]) + abs(point[1] - end[1])
        
        def is_valid(cell, start, end):
            if cell == start or cell == end:
                return True
            return 0 <= cell[0] < self.maze.rows and 0 <= cell[1] < self.maze.cols and self.maze.maze[cell[0]][cell[1]] == 0 #chua clear lam
        
        def astar(current, end):
            open_set = []
            # Priority queue with (F-score, node)
            heapq.heappush(open_set, (0,start))
            came_from = {}
            g_score = {start: 0}

            while open_set:
                _, current = heapq.heappop(open_set)
                self.visited_cells.append(current)
                if current == end:
                    path = []
                    while current in came_from:
                        path.append(current)
                        current = came_from[current]
                    path.append(start)  # Include the start point
                    path.reverse()  # Reverse the path to correct order
                    return path, self.visited_cells
                
                for dx,dy in [(-1,0), (0,1), (1,0), (0,-1)]:
                    next_cell = (current[0] + dx, current[1] + dy)
                    if not is_valid(next_cell, start, end):  
                        continue
                    new_g = g_score[current] + 1
                    if next_cell not in g_score or new_g < g_score[next_cell]:
                        g_score[next_cell] = new_g
                        f_score = new_g + heuristic(next_cell)
                        heapq.heappush(open_set, (f_score, next_cell))
                        came_from[next_cell] = current
            return None, self.visited_cells
        
        return astar(start, end)


        