from graph import movie_graph
from movies import movies

def bfs(graph, start):
    visited = set()
    que = [start]
    recc = []

    while que:
        now = que.pop(0)
        if now not in visited:
            visited.add(now)
            recc.append(now)
            for i in graph[now]:
                if i not in visited:
                    que.append(i)
    return recc
