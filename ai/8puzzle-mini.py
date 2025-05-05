from collections import deque
def print_board(board):
    for i in range(3):
        print(board[i*3:(i+1)*3])
    print()
def get_neighbors(board):
    neighbors = []
    zero_index = board.index(0)
    row, col = divmod(zero_index, 3)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_board = board[:]
            new_board[zero_index], new_board[new_index] = new_board[new_index], new_board[zero_index]
            neighbors.append(new_board)

    return neighbors

def is_goal(board):
    return board == [1, 2, 3, 4, 5, 6, 7, 8, 0]

def bfs(initial_board):
    queue = deque([(initial_board, [])])
    visited = set()

    while queue:
        current_board, path = queue.popleft()

        if is_goal(current_board):
            return path

        visited.add(tuple(current_board))

        for neighbor in get_neighbors(current_board):
            if tuple(neighbor) not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None  # No solution found

if __name__ == "__main__":
    initial_board = [1, 2, 3, 4, 5, 6, 0, 7, 8]  # Example initial state
    solution = bfs(initial_board)

    if solution is not None:
        print("Solution found:")
        for step in solution:
            print_board(step)
    else:
        print("No solution exists.")
