# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.
import functools
def product(array):
    result=[]
    for i in range(len(array)):
        result.append(functools.reduce(lambda a, b: a*b, array[:i]+array[i+1:]))
    return result

    

array=[1,2,3,4]
print(product(array))
