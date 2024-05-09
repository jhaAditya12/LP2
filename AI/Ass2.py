# 2. Implement Breadth First Search algorithm. Use an undirected graph and 
# develop a recursive algorithm for searching all the vertices of a graph or tree 
# data structure.




graph = {
    0: [1, 2, 3],
    1: [0, 4, 5],
    2: [0, 6],
    3: [0, 7],
    4: [],
    5: [],
    6: [],
    7: []
}


def bfs(graph, start_node):
    q = [start_node]
    visited_node = [start_node]
    while q:
        cur = q.pop(0)
        print(cur)
        for child_node in graph[cur]:
            if child_node not in visited_node:
                q.append(child_node)
                visited_node.append(child_node)


visited_node = [0] * 8
bfs(graph, 0)