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

    movie1 = request.args['movie1']
    movie2 = request.args['movie2']
    search_type = request.args['search_type']

    start = time.time()
    recommended_movies = get_rec_movie(conn, movie1, movie2, search_type)
    end = time.time()
    
    running_time = (end-start) * 10**3

    conn.close()
    return render_template("index.html", recommended_movies=recommended_movies, running_time = running_time) 


if __name__ == '__main__':
    app.run(debug=True)

