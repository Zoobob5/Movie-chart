from math import inf, sqrt
from heapq import heappop, heappush
from movies import movies
from graph import movie_graph
from bfs import bfs
from dfs import dfs


#print(movies)

def user_in(graph):
    user = input("Pick a recommended movie title: ").title().strip()
    if user:
        title = user.title()
        print(f"You picked: {title}")

    if title in graph:
        return title
    else:
        print("Movie not found. Please tyhpe in a listed movie.")
        return user_in(graph)

graph1 = movie_graph(movies)
print(graph1)
user_in(graph1)
