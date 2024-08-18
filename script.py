from math import inf, sqrt
from heapq import heappop, heappush
from movies import movies
from graph import movie_graph
from bfs import bfs
from dfs import dfs


#print(movies)
graph1 = movie_graph(movies)
print(graph1)
def user_in(graph):
    print(graph1)
    user = input("Pick a recommended movie title: ")
    if user in graph:
        recc = bfs(graph, user)
        if recc:
            print("Movies similar or related to {}".format(user))
            for i in recc:
                print(i)

        else:
            print("{} is not in the recommended list, please pick a recommended movie".format(user))
            return user_in()

user_in()
