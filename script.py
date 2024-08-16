from math import inf, sqrt
from heapq import heappop, heappush
from movies import movies
from graph import movie_graph


#print(movies)
graph = movie_graph(movies)
print(graph)
