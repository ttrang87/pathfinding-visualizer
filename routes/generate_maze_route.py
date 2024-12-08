from flask import Blueprint, request, jsonify
from maze_generation.kruskalmaze import MazeGenerator

generate_maze_blueprint = Blueprint('generate_kruskal', __name__)

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
            frame_array = []
            for r in range(rows):
                row = []
                for c in range(cols):
                    row.append(int(frame[r][c]))
                frame_array.append(row)
            frames.append(frame_array)
        
        maze_array = []
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(int(maze[r][c]))
            maze_array.append(row)

        return jsonify({
            "maze": maze_array,
            "steps": frames
        })

    maze = maze_generator.generate_maze()

    maze_array = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(int(maze[r][c]))
        maze_array.append(row)

    return jsonify({
        "maze": maze_array,
    })
