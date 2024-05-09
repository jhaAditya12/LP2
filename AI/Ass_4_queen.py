def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False
        # Check diagonals
        if abs(board[i] - col) == row - i:
            return False
    return True

def solve_n_queens_backtracking(n):
    def backtrack(row):
        if row == n:
            return True

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                if backtrack(row + 1):
                    return True

        return False

    board = [-1] * n
    if backtrack(0):
        return board
    else:
        return None

def print_solution(board):
    if board is None:
        print("No solution exists.")
    else:
        for row in board:
            print(" ".join('Q' if i == row else '.' for i in range(len(board))))

# Example usage:
n = int(input("Enter the number of Queens :"))  # Change this to the desired number of queens
solution = solve_n_queens_backtracking(n)
print("Backtracking Solution:")
print_solution(solution)
