from graph import movie_graph
from movies import movies

def dfs(graph, start):
    visit = set()
    stack = [start]
    rec = []

    while stack:
        now = stack.pop()
        if now not in visit:
            visit.add(now)
            rec.append(now)
            for i in graph[now]:
                if i not in visit:
                    stack.append(i)

    return rec
