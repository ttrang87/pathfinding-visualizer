from flask import Blueprint, request, jsonify
from maze_generation.kruskalmaze import KruskalMazeGenerator
from maze_generation.verticalmaze import VerticalMazeGenerator
from maze_generation.horizontalmaze import HorizontalMazeGenerator
from maze_generation.randommaze import RandomMazeGenerator

maze_blueprint = Blueprint('maze', __name__)

def generate_maze_response(generator_class, data):
    rows = data.get('rows')
    cols = data.get('cols')
    start = data.get('start')
    end = data.get('end')
    animate = data.get('animate', False)

    if rows < 5 or rows > 50 or cols < 5 or cols > 50:
        return jsonify({"error": "Maze dimensions must be between 5 and 50"}), 400

    maze_generator = generator_class(rows, cols, start, end)

    if animate:
        maze = maze_generator.generate_maze()
        frames = [
            [[int(cell) for cell in row] for row in frame]
            for frame in maze_generator.frames
        ]
        maze_array = [[int(cell) for cell in row] for row in maze]

        return jsonify({
            "maze": maze_array,
            "steps": frames
        })

    maze = maze_generator.generate_maze()
    maze_array = [[int(cell) for cell in row] for row in maze]

    return jsonify({
        "maze": maze_array,
    })

@maze_blueprint.route('/kruskal', methods=['POST'])
def kruskal_maze():
    data = request.json
    return generate_maze_response(KruskalMazeGenerator, data)

@maze_blueprint.route('/vertical', methods=['POST'])
def vertical_maze():
    data = request.json
    return generate_maze_response(VerticalMazeGenerator, data)

@maze_blueprint.route('/horizontal', methods=['POST'])
def horizontal_maze():
    data = request.json
    return generate_maze_response(HorizontalMazeGenerator, data)

@maze_blueprint.route('/random', methods=['POST'])
def random_maze():
    data = request.json
    return generate_maze_response(RandomMazeGenerator, data)
