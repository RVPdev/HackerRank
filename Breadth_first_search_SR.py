from collections import deque

def bfs(n, m, edges, s):
    # Creating an adjacency list to represent the graph. This list is indexed from 0 to n,
    # where each index i contains a list of nodes connected to node i.
    graph = [[] for i in range(n+1)]
    
    # Fill the adjacency list with the edges provided. Since the graph is undirected,
    # both directions are added for each edge.
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
        
    # A list to track whether a node has been visited or not, initialized to False for all nodes.
    visited = [False] * (n+1)
    
    # This list will hold the shortest distances from the starting node s to all other nodes.
    # It is initialized with -1, indicating that initially all nodes are considered unreachable.
    distances = [-1] * (n+1)
    
    # Initialize the queue with the starting node s, along with its current distance 0.
    q = deque([(s, 0)])
    
    # Set the distance of the starting node to itself as 0 and mark it as visited.
    distances[s] = 0
    visited[s] = True
    
    # Main loop of the BFS. Continue until there are no more nodes to process in the queue.
    while q:
        # Dequeue the front of the queue, getting the current node u and its associated distance w.
        u, w = q.popleft()
        
        # Iterate over each neighbor v of node u.
        for v in graph[u]:
            # If the neighbor has not been visited,
            if not visited[v]:
                # Set the distance to this neighbor as the current node's distance + 6 (given problem's edge weight).
                distances[v] = w + 6
                # Mark this neighbor as visited.
                visited[v] = True
                # Enqueue the neighbor along with its calculated distance for further exploration.
                q.append((v, w + 6))
                
    # Since the distance of the starting node to itself is not required, it is removed from the list.
    distances.remove(0)
    
    # Return the list of distances, starting from the node 1 (ignoring the index 0 which is unused in 1-based indexing).
    return distances[1:]
