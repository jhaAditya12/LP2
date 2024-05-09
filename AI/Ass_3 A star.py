class Graph:
    def __init__(self, adjac_list):
        self.adjac_list = adjac_list

    def get_neighbors(self, v):
        return self.adjac_list[v]

    def h(self, n):
        # Heuristic function should return heuristic value for node n
        # This can vary depending on the problem domain
        H = {'A': 1, 'B': 1, 'C': 1, 'D': 1}
        return H[n]

    def A_Star(self, start, stop):
        open_list = set([start])  # Set of nodes which have been visited but whose neighbors haven't been evaluated
        closed_list = set()       # Set of nodes whose neighbors have been evaluated
        distances = {}            # Dictionary to store distances from start node to other nodes
        distances[start] = 0
        parent = {}               # Dictionary to store parent nodes in the path
        parent[start] = start

        while open_list:
            current_node = None

            # Find node with the lowest value of f(n) = g(n) + h(n)
            for v in open_list:
                if current_node is None or (distances[v] + self.h(v)) < (distances[current_node] + self.h(current_node)):
                    current_node = v

            if current_node is None:
                print('Path does not exist!')
                return None

            # If the current node is the goal node, reconstruct and return the path
            if current_node == stop:
                reconst_path = []
                while parent[current_node] != current_node:
                    reconst_path.append(current_node)
                    current_node = parent[current_node]
                reconst_path.append(start)
                reconst_path.reverse()
                print('Path found: {}'.format(reconst_path))
                return reconst_path

            open_list.remove(current_node)
            closed_list.add(current_node)

            # Explore neighbors of the current node
            for neighbor, weight in self.get_neighbors(current_node):
                if neighbor in closed_list:
                    continue

                tentative_distance = distances[current_node] + weight
                if neighbor not in open_list or tentative_distance < distances[neighbor]:
                    parent[neighbor] = current_node
                    distances[neighbor] = tentative_distance
                    open_list.add(neighbor)

        print('Path does not exist!')
        return None

# Input
adjac_list = {'S': [('A', 3), ('B', 2)],
              'A': [('B', 3), ('D', 3), ('C', 1)],
              'B': [('D', 3), ('C', 5)],
              'C': [('D', 2)]}
graph1 = Graph(adjac_list)
graph1.A_Star('S', 'D')
