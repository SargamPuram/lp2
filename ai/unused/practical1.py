from collections import deque

# -------------------------
# INPUT GRAPH DYNAMICALLY
# -------------------------
graph = {}
n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

print("Enter each edge in the format: u v")
for _ in range(e):
    u, v = input("Edge: ").split()
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)  # Undirected graph

# -------------------------
# BFS FUNCTION
# -------------------------
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# -------------------------
# ITERATIVE DFS FUNCTION
# -------------------------
def iterative_dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# -------------------------
# DRIVER CODE
# -------------------------
start_node = input("Enter starting node: ")

print("\nBFS Traversal:")
bfs(graph, start_node)

print("\nDFS Traversal:")
iterative_dfs(graph, start_node)


# Enter number of nodes: 6
# Enter number of edges: 7
# Enter each edge in the format: u v
# Edge: A B
# Edge: A C
# Edge: B D
# Edge: B E
# Edge: C F
# Edge: D E
# Edge: E F
# Enter starting node: A
