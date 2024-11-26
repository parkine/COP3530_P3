from obj.Movie import Movie
from obj.Graph import Graph
from typing import Dict, List

def get_rec_movie(conn, movie1, movie2, search_type) -> str:
    c = conn.cursor()
    #LIKE condition to be case-sensitive
    c.execute('PRAGMA case_sensitive_like=ON;')

    # c.execute(r"SELECT * FROM movie WHERE primaryTitle = '(?)'", (movie1,))
    c.execute('SELECT * FROM movie WHERE primaryTitle = (?)', (movie1,))
    movie1Info = c.fetchone()

    c.execute('SELECT * FROM movie WHERE primaryTitle = (?)', (movie2,))
    movie2Info = c.fetchone()

    #m1 & m2 are Movie obj
    m1 = movie_obj(movie1Info)
    m2 = movie_obj(movie2Info)
    
    #fetch movies that are similar to m1 and m2
    c.execute(sql_related_movies(m1, m2.tconst))
    m1_list = c.fetchall()

    c.execute(sql_related_movies(m2, m1.tconst))
    m2_list = c.fetchall()

    #from_obj_dict and to_obj_dict are Dict[tconst, Movie obj]
    m1_obj_dict = movie_obj_list(m1_list)
    m2_obj_dict = movie_obj_list(m2_list)

    # Create a Graph obj
    graph = Graph(m1, m2, m1_obj_dict, m2_obj_dict)
    # Connect edges based on similar categories
    graph.connect_edge()

    if(search_type == 'DFS'):
        top_movies_tconst = graph.DFS()  
    else:
        top_movies_tconst = graph.BFS()    

    c.execute(sql_movie_list(top_movies_tconst))
    result = c.fetchall()
    
    return result

#input: tuple of movie information; output: movie object
def movie_obj(m_info) -> Movie:

    tconst = m_info[0].strip("'")
    title = m_info[1].strip("'")
    startYear = m_info[2] if m_info[2] is not None else 0
    runtimeMinutes = m_info[3] if m_info[3] is not None else 0
    genres = m_info[4].strip("'").split(',')
    rate = m_info[5] if m_info[5] is not None else 0
    if m_info[7] is not None:
        director = m_info[7].strip("'").split(',')
    else:
        director = []
    if  m_info[8] is not None:   
        writer = m_info[8].strip("'").split(',')
    else:
        writer = []

    movie = Movie(tconst, title, startYear, runtimeMinutes, genres, rate, director, writer)

    return movie 

#input: list of movie information(tuple), 2d tuple; output: Dict[tconst, Movie obj]
def movie_obj_list(m_list:List) -> Dict[str,Movie]:
    dict = {}
    for m in m_list:
        movie = movie_obj(m)
        dict[movie.tconst] = movie

    return dict

#build an SQL query that finds similar movies to movie, but exclude 1 movie (tconst) 
#TODO: build a proper sql 
def sql_related_movies(movie:Movie, tconst2:str) -> str:
    sql = f"SELECT * FROM movie WHERE startYear BETWEEN {movie.startYear-10} AND {movie.startYear+10}"
    sql += " AND averageRating >= 7 AND numVotes >= 100"   
    sql += f" AND runtimeMinutes BETWEEN {movie.runtimeMinutes-20} AND {movie.runtimeMinutes+20}"
    
    #JUST TO TEST
    # sql = f"SELECT * FROM movie WHERE startYear = 1950"    

    sql += " AND ("
    for genre in movie.genres:
        sql += f" genres LIKE '%{genre.lstrip(' ')}%' OR"

    sql = sql[:-2]
    sql += ") OR ("
        
    for d in movie.director:
        sql += f" directorName LIKE '%{d.lstrip(' ')}%' OR" 

    for w in movie.writer:
        sql += f" writerName LIKE '%{w.lstrip(' ')}%' OR" 
    
    sql = sql[:-2]
    sql += ")"

    sql += f" EXCEPT SELECT * FROM movie WHERE tconst = '{movie.tconst}' OR tconst = '{tconst2}'"

    print(sql)    
    return sql

def sql_movie_list(top_movies_tconst:List[str]) -> str:
    tconst_list = ', '.join(f"'{t}'" for t in top_movies_tconst)

    sql = f"SELECT * FROM movie WHERE tconst IN ({tconst_list});"

    return sql