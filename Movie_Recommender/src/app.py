from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from services.service import get_rec_movie
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movie', methods=['GET'])
def get_movie():
    conn = sqlite3.connect('./db/cop3530.db')

    movie1 = request.args.get('movie1', '').strip()
    movie2 = request.args.get('movie2', '').strip()
    search_type = request.args.get('search_type', '').strip()

    # validation
    if not movie1 or not movie2 or search_type not in ['DFS', 'BFS']:
        error = "Please provide valid movie titles and select a search type."
        return render_template('index.html', error=error)

    start = time.time()
    response = get_rec_movie(conn, movie1, movie2, search_type)
    end = time.time()
    running_time = (end - start) * 10**3

    conn.close()

    # errors in the response
    if "error" in response:
        error = response["error"]
        return render_template("index.html", error=error)
    else:
        recommended_movies = response["result"]
        return render_template("index.html", recommended_movies=recommended_movies, running_time=running_time)


if __name__ == '__main__':
    app.run(debug=True)