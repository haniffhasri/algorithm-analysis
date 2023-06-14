# This is a greedy search algorithm.

# inside plan
# n=null
# s=stair
# l=library
# c=courtyard
# k=kitchen
# b=balcony
# u=utility
# m=main hall
# d=dining
# e=entrance
# r1=room 1
# r2=room 2
# r3=room 3
# mb=master bedroom
# v=void

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

target_value = "end"

def greedy_search_2d(arr, target):
    for row in arr:
        for element in row:
            if element == target:
                return True
    return False

# Define the order of room priority based on proximity to the starting point
room_priority = ["s", "l", "c", "k", "d", "m", "e", "n", "u", "b", "r1", "r2", "r3", "mb"]

def greedy_search_2d_with_priority(arr, target, priority):
    for room in priority:
        for row in arr:
            for element in row:
                if element == room:
                    return True
    return False

if greedy_search_2d_with_priority(groundF, target_value, room_priority):
    print("All the rooms in ground floor have been checked.")
else:
    print("Not everything has been checked.")

if greedy_search_2d_with_priority(firstF, target_value, room_priority):
    print("All the rooms in first floor have been checked.")
else:
    print("Not everything has been checked.")
