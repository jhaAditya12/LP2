def dfs(adjList, startNode, visited):
    # Create a stack for DFS
    stack = []

    # Mark the current node as visited and push it onto the stack
    visited[startNode] = True
    stack.append(startNode)

    # Iterate over the stack
    while stack:
        # Pop a vertex from stack and print it
        currentNode = stack.pop()
        print(currentNode, end=" ")

        # Get all adjacent vertices of the popped vertex
        # If an adjacent has not been visited, then mark it visited and push it onto the stack
        for neighbor in adjList[currentNode]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
                # print()

# Add edge
def addEdge(adjList, u, v):
    adjList[u].append(v)



# Number of vertices in the graph
vertices = 5

# Adjacency list representation of the graph
adjList = [[] for _ in range(vertices)]

# Add edges to the graph
addEdge(adjList, 0, 1)
addEdge(adjList, 0, 2)
addEdge(adjList, 0, 3)
addEdge(adjList, 2, 3)
addEdge(adjList, 2, 4)


# Mark all the vertices as not visited
visited = [False] * vertices

# Perform DFS traversal starting from vertex 0
print("Depth First Traversal starting from vertex 0:", end=" ")
dfs(adjList, 0, visited)
