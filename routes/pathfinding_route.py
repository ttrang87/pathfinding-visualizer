from flask import Blueprint, request, jsonify
from pathfinding.share import Maze, Cell
from pathfinding.dfs import Depth_First_Search
from pathfinding.bfs import Breadth_First_Search
from pathfinding.astar import A_Star
from pathfinding.dijkstra import Dijkstra

import time

pathfinding_blueprint = Blueprint('pathfinding_1', __name__)

# Helper function for common logic
def solve_pathfinding_1(algorithm_class, data):
    maze_data = data.get('maze') 
    start_data = data.get('start')  
    end_data = data.get('end') 

    if not maze_data or not start_data or not end_data:
        return jsonify({"error": "Maze, start, and end data are required"}), 400

    maze = Maze(maze_data)
    start = Cell(start_data[0], start_data[1])
    end = Cell(end_data[0], end_data[1])

    solver = algorithm_class(maze)
    start_time = time.perf_counter()
    path, visited_cells = solver.search(start, end)
    end_time = time.perf_counter()

    duration = (end_time - start_time)*1000

    if path:
        return jsonify({"path": path, "visited_cells": visited_cells, "time": duration})
    else:
        return jsonify({"error": "No path found"}), 404

def solve_pathfinding_2(algorithm_class, data, runs = 10):
    maze_data = data.get('maze') 
    start_data = data.get('start')  
    end_data = data.get('end') 

    if not maze_data or not start_data or not end_data:
        return jsonify({"error": "Maze, start, and end data are required"}), 400

    maze = Maze(maze_data)
    start = tuple(start_data)
    end = tuple(end_data)

    solver = algorithm_class(maze)
    start_time = time.perf_counter()
    path, visited_cells = solver.search(start, end)
    end_time = time.perf_counter()

    duration = (end_time - start_time)*1000

    if path:
        return jsonify({"path": path, "visited_cells": visited_cells, "time": duration})
    else:
        return jsonify({"error": "No path found"}), 404

# Routes
@pathfinding_blueprint.route('/dfs', methods=['POST'])
def dfspath():
    data = request.json
    return solve_pathfinding_1(Depth_First_Search, data)

@pathfinding_blueprint.route('/bfs', methods=['POST'])
def bfspath():
    data = request.json
    return solve_pathfinding_1(Breadth_First_Search, data)

@pathfinding_blueprint.route('/astar', methods=['POST'])
def astarpath():
    data = request.json
    return solve_pathfinding_2(A_Star, data)

@pathfinding_blueprint.route('/dijkstra', methods=['POST'])
def dijkstrapath():
    data = request.json
    return solve_pathfinding_2(Dijkstra, data)
