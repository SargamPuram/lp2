from collections import deque

# Goal state for the 8 puzzle
GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Directions for moving the blank space (0) up, down, left, right
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid_move(state, x, y):
    return 0 <= x < 3 and 0 <= y < 3

def get_possible_moves(state):
    # Find the position of the blank space (0)
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return -1, -1

def apply_move(state, x1, y1, x2, y2):
    new_state = [row[:] for row in state]  # Create a copy of the state
    new_state[x1][y1], new_state[x2][y2] = new_state[x2][y2], new_state[x1][y1]
    return new_state

def bfs(start_state):
    start_state_tuple = tuple(tuple(row) for row in start_state)  # Convert to tuple for immutability and hashing
    goal_state_tuple = tuple(tuple(row) for row in GOAL_STATE)
    
    # If the starting state is already the goal state
    if start_state_tuple == goal_state_tuple:
        return []

    # BFS setup
    queue = deque([(start_state, [])])  # (state, moves)
    visited = set([start_state_tuple])

    while queue:
        current_state, path = queue.popleft()
        
        # Get the position of the blank space
        x, y = get_possible_moves(current_state)
        
        # Try all possible moves (up, down, left, right)
        for dx, dy in DIRECTIONS:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(current_state, new_x, new_y):
                # Apply the move
                new_state = apply_move(current_state, x, y, new_x, new_y)
                new_state_tuple = tuple(tuple(row) for row in new_state)
                
                # Check if we've already visited this state
                if new_state_tuple not in visited:
                    visited.add(new_state_tuple)
                    new_path = path + [(x, y, new_x, new_y)]
                    
                    # If the new state is the goal state, return the path
                    if new_state_tuple == goal_state_tuple:
                        return new_path
                    
                    queue.append((new_state, new_path))
    return None  # No solution found

def print_solution(path, start_state):
    # Start from the initial state and apply the moves
    current_state = start_state
    print("Initial state:")
    for row in current_state:
        print(row)
    
    for move in path:
        x1, y1, x2, y2 = move
        # Apply move
        current_state = apply_move(current_state, x1, y1, x2, y2)
        print(f"\nMove blank from ({x1}, {y1}) to ({x2}, {y2}):")
        for row in current_state:
            print(row)

if __name__ == "__main__":
    # Define the initial state of the puzzle
    start_state = [[1, 2, 3], [5, 6, 0], [4, 7, 8]]
    
    # Solve the puzzle using BFS
    path = bfs(start_state)
    
    if path:
        print("Solution found:")
        print_solution(path, start_state)
    else:
        print("No solution exists.")

