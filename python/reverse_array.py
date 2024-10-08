# Given an unsorted array arr[] of size n. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. 

# Examples :

# Input: n = 5, d = 2 arr[] = {1,2,3,4,5}
# Output: 3 4 5 1 2
# Explanation: 1 2 3 4 5  when rotated by 2 elements, it becomes 3 4 5 1 2.

# Example 2:

# Input: n = 10, d = 3 arr[] = {2,4,6,8,10,12,14,16,18,20}
# Output: 8 10 12 14 16 18 20 2 4 6
# Explanation: 2 4 6 8 10 12 14 16 18 20 when rotated by 3 elements, it becomes 8 10 12 14 16 18 20 2 4 6.

# Your Task:
# You need not print or read anything. You need to complete the function rotateArr() which takes the array, d and n as input parameters and rotates the array by d elements. The array must be modified in-place without using extra space.

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 <= n <= 106
# 1 <= d <= 106
# 0 <= arr[i] <= 105
def reverse_array(array, num_of_rotations):
    last_index=len(array)-1
    copied_elem=array[last_index]
    for index, elem in reversed(list(enumerate(array))):
        if index<num_of_rotations:
            array[last_index-(index+num_of_rotations)]
        else:
            remembered_elem=array[index-1]
            array[index-1]=copied_elem
            copied_elem=remembered_elem
    return array

def reverse_array_2(array, num):
    size=len(array)
    for i in (range(len(array))):
        move=(i-num)
        if move<0:
            move=move+size 
        array[move], array[i]=array[i], array[move]
        # if (i<num):
        #     array[size-i-1]=array[i]
        # ret
    return array

def rotateArr(arr, d, n):
    
    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    d = d % n
    reverse(arr, 0, d-1)
    reverse(arr, d, n-1)
    reverse(arr, 0, n-1)
    return arr



if __name__=='__main__':
    print(rotateArr([1,2,3,4,5], 2, 5))
    
# Output: 3 4 5 1 2