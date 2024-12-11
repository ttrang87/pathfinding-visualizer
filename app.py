from flask import Flask, render_template
from routes.generate_maze_route import generate_maze_blueprint
from routes.pathfinding_route import dfs_blueprint, bfs_blueprint, astar_blueprint, dijkstra_blueprint

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(generate_maze_blueprint, url_prefix="/maze")
app.register_blueprint(dfs_blueprint, url_prefix="/pathfinding")
app.register_blueprint(bfs_blueprint, url_prefix="/pathfinding")
app.register_blueprint(astar_blueprint, url_prefix="/pathfinding")
app.register_blueprint(dijkstra_blueprint, url_prefix="/pathfinding")

if __name__ == '__main__':
    app.run(debug=True)
