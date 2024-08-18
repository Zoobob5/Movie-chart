from math import inf, sqrt
from heapq import heappop, heappush
from movies import movies
from graph import movie_graph
from bfs import bfs


#print(movies)
graph = movie_graph(movies)
print(graph)
