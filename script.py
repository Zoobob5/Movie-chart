from math import inf, sqrt
from heapq import heappop, heappush
from movies import movies
from graph import movie_graph
from bfs import bfs
from dfs import dfs


#print(movies)

def user_in(graph):
    user = input("Pick a recommended full movie title: ").title().strip()
    if user:
        title = user.title()
        print(f"You picked: {title}")

    if title in graph:
        return title
    else:
        print("Movie not found. Please tyhpe in a listed movie.")
        return user_in(graph)

def valid_search():
    search = input("Choose search style, BFS (Breadth) or DFS (Depth): ").upper()
    if search == "BFS" or search == "DFS":
        return search
    else:
        print("Please pick a valid search option.")
        return valid_search()

def again():
    ask = input("Would you like to search for another movie recomendation? Please pick Yes or No: ").title().strip()

    if ask == "Yes":
        return get_rec()
    elif ask == "No":
        print("Thank you, have a good day.")
    else:
        print("Please pick a valid option.")
        return again()

def get_rec():
    #the graph
    graph1 = movie_graph(movies)
    #show the graph
    print(graph1)
    #get movie from person
    user = user_in(graph1)
    #pick search style
    search = valid_search()

    if search == "BFS":
        rec = bfs(graph1, user)
    elif search == "DFS":
        rec = dfs(graph1, user)


    if rec:
        print("{} is related to: ".format(user))
        if len(rec) <= 1:
            print(f"There are no other movies related to {rec[0]}")

        for i in rec:
            print(i)
    again()




#BEGIN
get_rec()
