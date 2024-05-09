class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def is_safe(self, v, color, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and color[i] == c:
                return False
        return True

    def graph_coloring_backtracking(self, m, color, v):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.is_safe(v, color, c):
                color[v] = c
                if self.graph_coloring_backtracking(m, color, v + 1):
                    return True
                color[v] = 0

        return False

    def mrv_heuristic(self, color, v):
        available_colors = [True] * (v + 1)

        for i in range(v):
            if self.graph[v][i] == 1 and color[i] != 0:
                available_colors[color[i]] = False

        for c in range(1, len(available_colors)):
            if available_colors[c]:
                return c

        return 1  # If no color available, return the first color

    def graph_coloring_branch_and_bound(self, m, color, v):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.is_safe(v, color, c):
                color[v] = c
                if self.graph_coloring_branch_and_bound(m, color, v + 1):
                    return True
                color[v] = 0

        return False

    def graph_coloring(self, m):
        color = [0] * self.V
        if self.graph_coloring_backtracking(m, color, 0):
            print("Solution exists for Backtracking:")
            print("Coloring of vertices:", color)
        else:
            print("No solution exists for Backtracking.")

        color = [0] * self.V
        if self.graph_coloring_branch_and_bound(m, color, 0):
            print("\nSolution exists for Branch and Bound:")
            print("Coloring of vertices:", color)
        else:
            print("No solution exists for Branch and Bound.")

# Example usage:
if __name__ == "__main__":
    g = Graph(4)
    g.graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    
    m = 3  # Number of colors
    g.graph_coloring(m)
