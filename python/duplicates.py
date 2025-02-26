# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def detect_duplicate_set(array):
    test_set=set(array)
    if len(test_set)==len(array):
        return False
    return True

array=[1,2,3,4]
print(detect_duplicate_set(array))
 
