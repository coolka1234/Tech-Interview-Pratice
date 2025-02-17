# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

def remove_duplicates(array):
    duplicates=0
    prev=None
    size_of_arr=len(array)
    eleme_num=0
    while eleme_num < size_of_arr:
        if array[eleme_num]==prev:
            duplicates+=1
        else:
            duplicates=0
        prev=array[eleme_num]
        if duplicates>=2:
            j=eleme_num
            while j < size_of_arr-1:
                array[j]=array[j+1]
                j+=1
            eleme_num-=1
            del array[-1:]
            size_of_arr-=1
        eleme_num+=1
    return array




if __name__ == '__main__':
    print(remove_duplicates([1,1,1,2,2,3])) # 5
    print(remove_duplicates([0,0,1,1,1,1,2,3,3])) # 7


