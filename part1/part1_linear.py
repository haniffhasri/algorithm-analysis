# This is a linear search algorithm.

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

# outside plan
# rw=right wing
# g=garden
# lw=left wing
# mBuilding=main building
# f=fish pond
# carG=car garage
# barn=barn
# gs=garden shed
# gh=green house
# bs=boat shed

propertyL = [["n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"],
             ["n", "rw", "n", "g", "g", "g", "g", "g", "n", "lw", "n", "barn", "barn", "n", "n", "n", "n", "n", "n"],
             ["n", "rw", "n", "g", "g", "g", "g", "g", "n", "lw", "n", "barn", "barn", "n", "n", "n", "n", "n", "n"],
             ["n", "rw", "n", "n", "n", "n", "n", "n", "n", "lw", "n", "n", "n", "gh", "n", "n", "n", "n", "n"],
             [
                 "n", "rw", "rw", "n", "mBuilding", "mBuilding", "mBuilding", "n", "lw", "lw", "n", "gs", "n", "gh", "n", "n", "n", "n", "n"],
             [
                 "n", "n", "n", "n", "mBuilding", "mBuilding", "mBuilding", "n", "n", "n", "n", "n", "n", "gh", "n", "n", "n", "n", "n"],
             ["n", "n", "n", "n", "n", "n", "n", "n", "carG", "carG", "n", "n", "n", "gh", "n", "n", "n", "n", "n"],
             ["n", "n", "n", "n", "f", "f", "f", "n", "carG", "carG", "n", "n", "n", "n", "n", "n", "n", "n", "n"],
             ["n", "n", "n", "n", "f", "f", "f", "n", "n", "n", "n", "n", "bs", "n", "n", "n", "n", "n", "n"],
             ["n", "n", "n", "n", "f", "f", "f", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"],
             ["n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"],
             ["n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"],
             ["n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"],
             ["n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "end"]]

target_value="end"

def linear_search_2d(arr, target):
    for row in arr:
        for element in row:
            if element == target:
                return True
    return False

if linear_search_2d(groundF, target_value):
    print("Everything has been checked.")
else:
    print("Not everything has been checked.")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
