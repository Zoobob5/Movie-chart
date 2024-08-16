from movies import movies

def movie_graph(set_movies):
    graph = {}
    for movie, detail in set_movies.items():
        graph[movie] = []
        for movie2, detail2 in set_movies.items():
            if movie != movie2 and (detail["genre"] == detail2["genre"] or detail["director"] == detail2["director"] or set(detail["actors"]) & set(detail2["actors"])):
                graph[movie].append(movie2)
    return graph
