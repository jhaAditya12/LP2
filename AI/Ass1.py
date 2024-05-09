# 1. Implement Depth First Search algorithm (DFS). Use an undirected graph and 
# develop a recursive algorithm for searching all the vertices of a graph or tree 
# data structure.

graph = {
    0: [1, 2, 3],
    1: [0, 4, 5],
    2: [0, 6],
    3: [0, 7],
    4:[ ],
    5:[ ],
    6:[ ],
    7:[ ],
}

print("Depth-First Search.")
def dfs(graph,start_node):
    visited_node[start_node] = 1
    print(start_node)

    for child_node in graph[start_node]:
        if not visited_node[child_node]:
            dfs(graph,child_node)



visited_node = [0] * 8
# print(vis)
dfs(graph, 0)