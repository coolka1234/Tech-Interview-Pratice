# Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 


def calc_water(arr):
    last_barricade=0
    total_water=0
    potential_water=0
    for block in arr:
        if block<last_barricade:
            potential_water+=last_barricade-block
        else:
            last_barricade=block
            total_water+=potential_water
    return total_water

arr=[3, 0, 1, 0, 4, 0, 2]
print()