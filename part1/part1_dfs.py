groundF = [["s", "l", "l", "c", "c", "c", "n", "k", "k", "b"],
           ["s", "l", "l", "c", "c", "c", "n", "k", "k", "b"],
           ["s", "l", "l", "c", "c", "c", "n", "d", "d", "b"],
           ["n", "n", "n", "n", "n", "n", "n", "d", "d", "b"],
           ["u", "m", "m", "m", "m", "m", "m", "d", "d", "b"],
           ["u", "m", "m", "m", "m", "m", "m", "d", "d", "b"],
           ["n", "n", "n", "n", "e", "e", "n", "n", "n", "n", "end"]]


firstF = [["s", "r1", "n", "v", "v", "v", "n", "r3", "r3", "b"],
          ["s", "r1", "n", "v", "v", "v", "n", "r3", "r3", "b"],
          ["s", "r1", "n", "v", "v", "v", "n", "r2", "r2", "b"],
          ["n", "n", "n", "n", "n", "n", "n", "r2", "r2", "b"],
          ["u", "mb", "mb", "mb", "mb", "mb", "mb", "r2", "r2", "b"],
          ["u", "mb", "mb", "mb", "mb", "mb", "mb", "r2", "r2", "b"],
          ["b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "end"]]


target_value="end"
def dfs_2d(arr, row, col, visited):
    # Check if the current position is out of bounds or has been visited
    if row < 0 or col < 0 or row >= len(arr) or col >= len(arr[0]) or visited[row][col]:
        return
    
    visited[row][col] = True
    
    # Check if the current room matches the target value
    if arr[row][col] == target_value:
        return
    
    # Explore adjacent rooms in a clockwise order: up, right, down, left
    dfs_2d(arr, row - 1, col, visited)  # Up
    dfs_2d(arr, row, col + 1, visited)  # Right
    dfs_2d(arr, row + 1, col, visited)  # Down
    dfs_2d(arr, row, col - 1, visited)  # Left


# Create a visited array to keep track of visited rooms
visited_groundF = [[False] * len(groundF[0]) for _ in range(len(groundF))]
visited_firstF = [[False] * len(firstF[0]) for _ in range(len(firstF))]

# Perform DFS on the ground floor
dfs_2d(groundF, 0, 0, visited_groundF)

# Perform DFS on the first floor
dfs_2d(firstF, 0, 0, visited_firstF)

# Check if all the rooms on the ground floor have been checked
if visited_groundF[-1][-1]:
    print("All the rooms on the ground floor have been checked.")
else:
    print("Not everything has been checked on the ground floor.")

# Check if all the rooms on the first floor have been checked
if visited_firstF[-1][-1]:
    print("All the rooms on the first floor have been checked.")
else:
    print("Not everything has been checked on the first floor.")