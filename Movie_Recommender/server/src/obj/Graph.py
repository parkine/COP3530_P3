from typing import Dict, List, Set, Tuple
from collections import deque
from obj.Movie import Movie

class Graph:
    #src is the user input1 & dest is the user input2
    #src_list is the list of movies that are related to src
    #dest_list is the list of movies that are related to dest
    def __init__(self, src:Movie, dest:Movie, src_list:Dict[str,Movie], dest_list:Dict[str,Movie]):
        self.src = src
        self.dest = dest
        #Dict[from_tconst, Dict[to_tconst, weight]]
        self.list: Dict[str, Dict[str,float]] = {}
        self.src_list = src_list
        self.dest_list = dest_list

    #calculate the weight based on criteria
    def cal_weight(self, m1:Movie, m2:Movie) -> float:
        w:float = 0

        #If the director is the same
        if(m1.dir == m2.dir):
            w += 5
        for g in m1.genre:
            if(g in m2.genre):
                w += 1
            
        return w


    # create edge
    def connect_edge(self):

        #initialize src into the dict
        self.list[self.src.tconst] = dict()

        # make connection from src + calculate weight
        
        # loop through the properties in the dict, src_list
        for s_tc, s_movie in self.src_list.items():
            #calculate the weight based on its similarity
            w:float = self.cal_weight(self.src, s_movie)

            #add the related movie 'to list' of src
            self.list[self.src.tconst][s_tc] = w

            #add the related movie itself into the 'from list'
            self.list[s_tc] = dict()

        #this will be the dict with {tconst:weight} that are related to src
        #e.g., {'tt0000006': 2, 'tt0000004': 1, 'tt0000008': 6}
        from_src_movies = self.list[self.src.tconst]
        
        #loop through the properties in the dict, dest_list
        for d_tc, d_movie in self.dest_list.items():
            
            #initialize the new dict in the list with tconst
            self.list[d_tc] = dict()
            #calculate the weight
            w:float = self.cal_weight(self.dest, d_movie)
            
            #We need to compare each 'related to dest movie' to each 'related to src movie    
 
            #the d_tc is NOT directly related to both src and dest
            # I have to find the connection between dest_m and list of from_src_movies -> loop
            if d_tc not in from_src_movies:
                for src_m in from_src_movies:
                    #If the src_m is related to d_tc
                    if self.cal_weight(self.src_list[src_m], d_movie)  != 0:
                        #Just make a connection, weight is not meaningful here
                        self.list[src_m][d_tc] = 0

            #Lastly, make connection from 'related to dest movie' to 'dest movie'
            self.list[d_tc][self.dest.tconst] = w

    def notVisited(self, tconst: str, path: List[Tuple[str, float]]) -> int:

        length = len(path)
        for i in range(length):
            if (path[i][0] == tconst):
                return 0
                
        return 1


    def BFS(self):
        q = deque()
        #path is list of tconst
        path: List[Tuple[str, float]] = []
        weights = dict()

        #initially put weight zero
        path.append((self.src.tconst,0))
        q.append(path)

        adj = {3:1, 4:0.8, 5:0.6}

        while q:
            path = q.pop()
            last = path[len(path)-1]

            #max path length is 5 for now 

            if last[0] == self.dest.tconst:
                #adjust weight based on the length of path
                w1 = path[1][1]*adj[len(path)]
                w2 = path[len(path)-1][1]*adj[len(path)]
                
                m1 = path[1][0]
                m2 = path[len(path)-1][0]
                
                #direct connection for both src and dest
                if(len(path) == 3):
                    w1 += w2

                for m,w in [(m1,w1),(m2,w2)]:
                    if(m in weights):
                        weights[m] = max(weights[m], w)
                    else:
                        weights[m] = w
                
                
                #TEST
                print(path)


            else:                
                #max path length is 5 for now
                if(len(path) < 5):
                    # key = tconst, value = weight
                    for tc, w in self.list[last[0]].items():
                         
                        if(self.notVisited(tc, path)):
                            new_path = path.copy()
                            new_path.append((tc, w))
                            q.append(new_path)

        print(weights)




    def DFS(self):
        q = deque()
        #path is list of tconst
        path: List[Tuple[str, float]] = []
        weights = dict()

        #initially put weight zero
        path.append((self.src.tconst,0))
        q.append(path)

        adj = {3:1, 4:0.8, 5:0.6}

        while q:
            path = q.popleft()
            last = path[len(path)-1]

            #max path length is 5 for now 

            if last[0] == self.dest.tconst:
                #adjust weight based on the length of path
                w1 = path[1][1]*adj[len(path)]
                w2 = path[len(path)-1][1]*adj[len(path)]
                
                m1 = path[1][0]
                m2 = path[len(path)-1][0]
                
                #direct connection for both src and dest
                if(len(path) == 3):
                    w1 += w2

                for m,w in [(m1,w1),(m2,w2)]:
                    if(m in weights):
                        weights[m] = max(weights[m], w)
                    else:
                        weights[m] = w
                
                
                #TEST
                print(path)


            else:                
                #max path length is 5 for now
                if(len(path) < 5):
                    # key = tconst, value = weight
                    for tc, w in self.list[last[0]].items():
                         
                        if(self.notVisited(tc, path)):
                            new_path = path.copy()
                            new_path.append((tc, w))
                            q.append(new_path)

        print(weights)




                
    def find_similar_movies(base_movie: Movie, all_movies: List[Movie]) -> List[Movie]:
        similar_movies = []
        for movie in all_movies:
            if movie is base_movie:  # Skip the base movie itself
                continue
            # Check if they share a director or at least one genre
            if movie.dir == base_movie.dir or any(genre in base_movie.genre for genre in movie.genre):
                similar_movies.append(movie)
        return similar_movies