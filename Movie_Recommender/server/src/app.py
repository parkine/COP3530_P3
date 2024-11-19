from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


#TODO: it makes a connection to the movies.db file which is sqlite
def create_database():
    conn = sqlite3.connect('../db/movies.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS movie (id INTEGER PRIMARY KEY, task TEXT)''')
    conn.commit()
    conn.close()

#TODO: connect it to the front end 

#TODO: Create service methods to process the movie list, calculate the weight, 
# make a list of recommended movies (probably 5) to return it to the front


