def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

# Backtracking approach
def is_safe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_backtracking(board, col, N):
    if col >= N:
        print_solution(board)
        return True

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            if solve_n_queens_backtracking(board, col + 1, N):
                return True
            board[i][col] = 0  # Backtrack

    return False

def n_queens_backtracking(N):
    board = [[0] * N for _ in range(N)]
    if not solve_n_queens_backtracking(board, 0, N):
        print("No solution exists")

# Branch and Bound approach
def is_safe_branch_bound(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_branch_bound(board, col, N, solutions):
    if col >= N:
        solutions.append([row[:] for row in board])
        return

    for i in range(N):
        if is_safe_branch_bound(board, i, col, N):
            board[i][col] = 1
            solve_n_queens_branch_bound(board, col + 1, N, solutions)
            board[i][col] = 0  # Backtrack

def n_queens_branch_bound(N):
    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_n_queens_branch_bound(board, 0, N, solutions)
    
    if not solutions:
        print("No solution exists")
    else:
        for solution in solutions:
            print_solution(solution)

# Example usage
N = 4
print("Backtracking Solution:")
n_queens_backtracking(N)

print("Branch and Bound Solutions:")
n_queens_branch_bound(N)


