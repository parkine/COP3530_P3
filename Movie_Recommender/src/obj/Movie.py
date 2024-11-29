from typing import List


class Movie:
    def __init__(self, tconst, title, startYear, runtimeMinutes, genres, rate, director, writer):
        self.tconst = tconst
        self.title = title
        self.startYear = startYear
        self.runtimeMinutes = runtimeMinutes
        self.genres = genres
        self.rate = rate
        self.director = director
        self.writer = writer


    # # Define __hash__ and __eq__ so that Movie objects can be added to a set
    # def __hash__(self):
    #     return hash(self.tconst)  # Hash based on tconst

    # def __eq__(self, other):
    #     if isinstance(other, Movie):
    #         return self.tconst == other.tconst  # Two movies are equal if tconst is the same
    #     return False

