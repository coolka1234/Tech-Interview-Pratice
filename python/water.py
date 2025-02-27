# Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 


def calc_water(arr):
    last_barricade=0
    total_water=0
    potential_water=0
    over_water=0
    for block in arr:
        if block<last_barricade:
            potential_water+=last_barricade-block
            over_water+=1
        else:
            last_barricade=block
            total_water+=potential_water
            potential_water=0
            over_water=0
    if over_water>0:
        total_water-=(over_water*(last_barricade-arr[-1]))        
        total_water+=potential_water
    return total_water

arr=[1,2,3,4]
print(calc_water(arr))
