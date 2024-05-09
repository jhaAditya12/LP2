from collections import deque

def bfs(adjList, startNode, visited):
    # Create a queue for BFS
    q = deque()

    # Mark the current node as visited and enqueue it
    visited[startNode] = True
    q.append(startNode)

    # Iterate over the queue
    while q:
        # Dequeue a vertex from queue and print it
        currentNode = q.popleft()
        print(currentNode, end=" ")

        # Get all adjacent vertices of the dequeued vertex
        # If an adjacent has not been visited, then mark it visited and enqueue it
        for neighbor in adjList[currentNode]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)


def addEdge(adjList, u, v):adjList[u].append(v)


# Number of vertices in the graph
vertices = 5

# Adjacency list representation of the graph
adjList = [[] for _ in range(vertices)]

# Add edges to the graph
addEdge(adjList, 0, 1)
addEdge(adjList, 0, 2)
addEdge(adjList, 1, 3)
addEdge(adjList, 1, 4)
addEdge(adjList, 2, 4)

# Mark all the vertices as not visited
visited = [False] * vertices

# Perform BFS traversal starting from vertex 0
print("Breadth First Traversal starting from vertex 0:", end=" ")
bfs(adjList, 0, visited)