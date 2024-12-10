from flask import Blueprint, request, jsonify
from pathfinding.dfs import Depth_First_Search, Cell, Maze  
from pathfinding.bfs import Breadth_First_Search

dfs_blueprint = Blueprint('dfspath', __name__)
bfs_blueprint = Blueprint('bfspath', __name__)


@dfs_blueprint.route('/dfs', methods=['POST'])
def dfspath():
    data = request.json
    maze_data = data.get('maze') 
    start_data = data.get('start')  
    end_data = data.get('end') 
    if not maze_data or not start_data or not end_data:
        return jsonify({"error": "Maze, start, and end data are required"}), 400

    maze = Maze(maze_data)
    start = Cell(start_data[0], start_data[1])
    end = Cell(end_data[0], end_data[1])

    dfs_solver = Depth_First_Search(maze)
    path, visited_cells = dfs_solver.search(start, end)
    if path:
        return jsonify({"path": path, "visited_cells": visited_cells})
    else:
        return jsonify({"error": "No path found"}), 404
    
@bfs_blueprint.route('/bfs', methods=['POST'])
def bfspath():
    data = request.json
    maze_data = data.get('maze') 
    start_data = data.get('start')  
    end_data = data.get('end') 
    if not maze_data or not start_data or not end_data:
        return jsonify({"error": "Maze, start, and end data are required"}), 400

    maze = Maze(maze_data)
    start = Cell(start_data[0], start_data[1])
    end = Cell(end_data[0], end_data[1])

    bfs_solver = Breadth_First_Search(maze)
    path, visited_cells = bfs_solver.search(start, end)
    if path:
        return jsonify({"path": path, "visited_cells": visited_cells})
    else:
        return jsonify({"error": "No path found"}), 404
