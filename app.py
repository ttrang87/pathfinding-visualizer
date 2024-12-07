from flask import Flask, render_template
from routes.generate_maze_route import generate_maze_blueprint

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(generate_maze_blueprint, url_prefix="/maze")

if __name__ == '__main__':
    app.run(debug=True)
