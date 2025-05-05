def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")  # Process the node
        visited.add(node)     # Mark the node as visited
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS Traversal:")
visited_dfs = set()
dfs(graph, 'A', visited_dfs)


print("\nBFS Traversal:")
bfs(graph, 'A')

