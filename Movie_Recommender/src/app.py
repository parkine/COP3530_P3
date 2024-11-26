from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from services.service import get_rec_movie
import time

app = Flask(__name__)


#TODO: it makes a connection to the movies.db file which is sqlite

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movie', methods=['GET'])
def get_movie():
    conn = sqlite3.connect('./db/cop3530.db')

    movie1 = request.args['movie1']
    movie2 = request.args['movie2']

    start = time.time()
    movie = get_rec_movie(conn, movie1, movie2)
    end = time.time()

    print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")

    conn.close()
    return render_template("index.html") 

# @app.route('/delete/<int:task_id>')
# def delete_task(task_id):
#     conn = sqlite3.connect('./db/cop3530.db')
#     c = conn.cursor()
#     c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
#     conn.commit()
#     conn.close()
#     return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)




#TODO: connect it to the front end 

#TODO: Create service methods to process the movie list, calculate the weight, 
# make a list of recommended movies (probably 5) to return it to the front


