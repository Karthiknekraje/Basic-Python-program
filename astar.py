def a_star(start, goal):
    # Initialize open set with start node, closed set as empty, and dictionaries to store g-values and parents
    open_set, closed_set, g, parents = {start}, set(), {start: 0}, {start: start}
    
    # Main loop of A* algorithm
    while open_set:
        # Choose the node with the minimum total cost (g + heuristic) from the open set
        current = min(open_set, key=lambda x: g[x] + H.get(x, float('inf')))
        
        # Check if the current node is the goal or if it's not in the graph
        if current == goal or current not in Graph:
            break
        
        # Explore neighbors of the current node
        for neighbor, weight in Graph[current]:
            # Calculate tentative g-value for the neighbor
            tentative_g = g[current] + weight
            
            # Update neighbor's g-value and parent if a shorter path is found
            if tentative_g < g.get(neighbor, float('inf')):
                if neighbor not in closed_set:  # If neighbor not in closed set, add to open set
                    open_set.add(neighbor)
                parents[neighbor], g[neighbor] = current, tentative_g
        
        # Move the current node from open set to closed set
        open_set.remove(current)
        closed_set.add(current)
    
    # Path reconstruction if goal node is found
    if current == goal:
        path = []
        while current != start:
            path.append(current)
            current = parents[current]
        path.append(start)
        print('Path found:', path[::-1])
        return path[::-1]
    
    # If goal node is not found
    print('Path does not exist!')
    return None

# Graph representation
Graph = {'A': [('B', 6), ('F', 3)], 'B': [('C', 3), ('D', 2)], 'C': [('D', 1), ('E', 5)], 'D': [('C', 1), ('E', 8)], 'E': [('I', 5), ('J', 5)], 'F': [('G', 1), ('H', 7)], 'G': [('I', 3)], 'H': [('I', 2)], 'I': [('E', 5), ('J', 3)]}

# Heuristic values for each node
H = {'A': 10, 'B': 8, 'C': 5, 'D': 7, 'E': 3, 'F': 6, 'G': 5, 'H': 3, 'I': 1, 'J': 0}

# Call the A* algorithm with start and goal nodes
a_star('A', 'J')
