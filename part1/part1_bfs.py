from collections import deque


def bfs(graph, start, destination):
    visited = set()
    queue = deque([(start, [])])

    while queue:
        current_node, path = queue.popleft()
        visited.add(current_node)

        if current_node == destination:
            return path + [current_node]

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [current_node]))

    return None


# Graph representation for the ground floor
ground_floor_graph = {
    'Stair to 1st floor': ['Library', 'Utility'],
    'Library': ['Stair to 1st floor', 'Courtyard', 'Main hall'],
    'Courtyard': ['Library', 'Kitchen', 'Main hall'],
    'Kitchen': ['Courtyard', 'Balcony', 'Dining'],
    'Balcony': ['Kitchen', 'Dining'],
    'Dining': ['Kitchen', 'Balcony', 'Main hall'],
    'Main hall': ['Library', 'Utility', 'Dining', 'Entrance'],
    'Utility': ['Stair to 1st floor', 'Main hall'],
    'Entrance': ['Main hall']
}

# Graph representation for the first floor
first_floor_graph = {
    'Stair to 1st floor': ['Room 1', 'Utility'],
    'Room 1': ['Stair to 1st floor', 'VOID', 'Master Bedroom'],
    'VOID': ['Room 1', 'Room 3', 'Master Bedroom'],
    'Room 3': ['VOID', 'Room 2'],
    'Room 2': ['Room 3', 'Master Bedroom'],
    'Master Bedroom': ['Room 1', 'VOID', 'Room 2','Utility'],
    'Utility': ['Stair to 1st floor', 'Master Bedroom'],
}

# Graph representation for the overall property
overall_property_graph = {
    'Right Wing': ['Garden', 'Main Building'],
    'Garden': ['Right Wing', 'Left Wing', 'Main Building'],
    'Left Wing': ['Garden', 'Main Building', 'Car Garage', 'Barn', 'Garden Shed'],
    'Barn': ['Left Wing', 'Green House', 'Garden Shed'],
    'Green House': ['Barn', 'Garden Shed', 'Boat Shed', 'Lake'],
    'Main Building': ['Right Wing', 'Garden', 'Left Wing', 'Car Garage', 'Fish Pond'],
    'Car Garage': ['Main Building', 'Left Wing', 'Fish Pond', 'Lake'],
    'Garden Shed': ['Left Wing', 'Barn', 'Green House'],
    'Fish Pond': ['Main Building', 'Car Garage', 'Lake'],
    'Boat Shed': ['Green House', 'Lake'],
    'Lake': ['Green House', 'Boat Shed', 'Car Garage', 'Fish Pond']
}

floor_level = input("Enter a place to search (ground floor/first floor/overall property): ")

if floor_level.lower() == 'ground floor':
    graph = ground_floor_graph
elif floor_level.lower() == 'first floor':
    graph = first_floor_graph
elif floor_level.lower() == 'overall property':
    graph = overall_property_graph
else:
    print("Invalid place provided. Please choose either 'ground floor', 'first floor or 'overall property' only.")
    exit()

start_place = input("Enter your starting place: ")
destination_place = input("Enter room/place you want to search: ")

path = bfs(graph, start_place, destination_place)

if path:
    print(f"The path to search {destination_place} from {start_place} on the {floor_level} is: {path}")
else:
    print(f"No path found from {start_place} to {destination_place} on the {floor_level}.")