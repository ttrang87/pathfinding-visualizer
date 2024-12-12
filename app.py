from flask import Flask, render_template
from routes.generate_maze_route import maze_blueprint
from routes.pathfinding_route import pathfinding_blueprint

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(maze_blueprint, url_prefix="/maze")
app.register_blueprint(pathfinding_blueprint, url_prefix="/pathfinding")


if __name__ == '__main__':
    app.run(debug=True)
