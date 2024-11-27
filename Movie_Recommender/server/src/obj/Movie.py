from typing import List


class Movie:
    def __init__(self, tconst:str, dir:str, genre:List[str]):
        self.tconst = tconst
        self.dir = dir
        self.genre = genre

    # Define __hash__ and __eq__ so that Movie objects can be added to a set
    def __hash__(self):
        return hash(self.tconst)  # Hash based on tconst

    def __eq__(self, other):
        if isinstance(other, Movie):
            return self.tconst == other.tconst  # Two movies are equal if tconst is the same
        return False



    # def get_movie_list(self) -> List["Movie"]:
    #     #fetch the information of list of movies that is relate to self from DB
    #     # OR if it's already fetched for UI, I can find in the fetched list
    #     # need to find how to fetch from the json list
    #     # make sure remove src, and dest movies from the list
    #     print("mya")

    # def update_weight(self, new_w:int):
    #     self.weight = new_w