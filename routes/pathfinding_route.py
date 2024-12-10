from flask import Blueprint, request, jsonify
from pathfinding.model import Maze, Cell
from pathfinding.dfs import Depth_First_Search
from pathfinding.bfs import Breadth_First_Search
from pathfinding.astar import A_Star

dfs_blueprint = Blueprint('dfspath', __name__)
bfs_blueprint = Blueprint('bfspath', __name__)
astar_blueprint = Blueprint('astarpath', __name__)


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

@astar_blueprint.route('/astar', methods=['POST'])
def astarpath():
    data = request.json
    maze_data = data.get('maze') 
    start_data = data.get('start')  
    end_data = data.get('end') 
    if not maze_data or not start_data or not end_data:
        return jsonify({"error": "Maze, start, and end data are required"}), 400

    maze = Maze(maze_data)
    start = tuple(start_data)
    end = tuple(end_data)

    print(start, end)

    astar_solver = A_Star(maze)
    path, visited_cells = astar_solver.search(start, end)
    print(path)
    if path:
        return jsonify({"path": path, "visited_cells": visited_cells})
    else:
        return jsonify({"error": "No path found"}), 404

