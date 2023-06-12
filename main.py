from flask import Flask, request, jsonify

app = Flask(__name__)

movies = []


@app.route('/')
def hello():
    return 'Welcome to flask movie api!'


@app.route('/movies')
def get_movies():
    return jsonify(movies)


@app.route('/movies/<int:id>')
def get_movie_by_id(id: int):
    if 0 < id <= len(movies):
        return movies[id-1]
    return 'Not found', 404


@app.route('/movies', methods=['POST'])
def add_movie():
    if 'title' not in request.json or 'release_year' not in request.json:
        return 'Bad request', 400

    new_movie = {'id': len(movies)+1,
                 'title': request.json['title'],
                 'description': request.json.get('description', ''),
                 'release_year': request.json['release_year']
                 }

    movies.append(new_movie)
    return movies[-1]


@app.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id: int):
    if 0 < id <= len(movies):
        movies[id-1]['title'] = request.json.get('title', movies[id-1]['title'])
        movies[id-1]['description'] = request.json.get('description', movies[id-1]['description'])
        movies[id-1]['release_year'] = request.json.get('release_year', movies[id-1]['release_year'])
        return movies[id-1]
    return 'Not found', 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
