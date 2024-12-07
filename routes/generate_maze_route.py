from flask import Blueprint, request, jsonify
from maze_generation.kruskalmaze import MazeGenerator

generate_maze_blueprint = Blueprint('generate_kruskal', __name__) #not affect the URL or functionality, just name.

@generate_maze_blueprint.route('/kruskal', methods=['POST'])
def generate_maze():
    data = request.json
    rows = data.get('rows')
    cols = data.get('cols')
    start = data.get('start')
    end = data.get('end')
    animate = data.get('animate', False)  

    if rows < 5 or rows > 50 or cols < 5 or cols > 50:
        return jsonify({"error": "Maze dimensions must be between 5 and 50"}), 400
    
    maze_generator = MazeGenerator(rows, cols, start, end)

    if animate:
        maze = maze_generator.generate_maze()
        frames = []
        for frame in maze_generator.frames:
            frame_dict = {}
            for r in range(rows):
                for c in range(cols):
                    frame_dict[f"{r},{c}"] = int(frame[r][c])
            frames.append(frame_dict)
        
        maze_dict = {}
        for r in range(rows):
            for c in range(cols):
                maze_dict[f"{r},{c}"] = int(maze[r][c])

        return jsonify({
            "maze": maze_dict,
            "steps": frames
        })

    maze = maze_generator.generate_maze()

    # Convert the maze to a dictionary with (row,col) keys
    maze_dict = {}
    for r in range(rows):
        for c in range(cols):
            maze_dict[f"{r},{c}"] = int(maze[r][c])

    return jsonify({
        "maze": maze_dict,
    })
