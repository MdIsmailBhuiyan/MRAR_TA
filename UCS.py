import heapq

def uniform_cost_search(start, goal, nodes):
    open_set = []
    heapq.heappush(open_set, (0, start))  # (cost, node)
    
    came_from = {}
    cost_so_far = {start: 0}
    
    # Define possible movements (up, down, left, right)
    movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    movement_names = ["up", "right", "down", "left"]

    while open_set:
        current_cost, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        # Explore neighbors
        for i, move in enumerate(movements):
            neighbor = (current[0] + move[0], current[1] + move[1])

            # Check if neighbor is in the list of valid nodes
            if neighbor in nodes:
                new_cost = current_cost + 1  # Assume cost of 1

                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    came_from[neighbor] = (current, movement_names[i])
                    heapq.heappush(open_set, (new_cost, neighbor))

    return None  # Path not found

def reconstruct_path(came_from, current):
    total_path = []
    while current in came_from:
        current_node, direction = came_from[current]
        total_path.append(direction)
        current = current_node
    return total_path[::-1]  # Return reversed path

# Example usage
nodes = [(x, y) for x in range(6) for y in range(6)]  # List of tuples from (0,0) to (5,5)
start = (0, 0)
goal = (5, 5)

path = uniform_cost_search(start, goal, nodes)
print("Path from {} to {}: {}".format(start, goal, path))
