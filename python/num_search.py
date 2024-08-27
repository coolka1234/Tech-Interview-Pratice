# Given an integer k and array arr. Your task is to return the position of the first occurrence of k in the given array and if element k is not present in the array then return -1.

# Note: 1-based indexing is followed here.

# Examples:

# Input: k = 16 , arr = [9, 7, 16, 16, 4]
# Output: 3
# Explanation: The value 16 is found in the given array at positions 3 and 4, with position 3 being the first occurrence.

# Input: k=98 , arr = [1, 22, 57, 47, 34, 18, 66]
# Output: -1
# Explanation: k = 98 isn't found in the given array.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 <= arr.size <= 106
# 1 <= arr[i] <= 109
# 1 <= k <= 106
def search(arr, k):
    for num, i in enumerate(arr, start=0):
        if i==k:
            return num+1
    return -1

if __name__=='__main__':
    arr=[9,7,16,16,4]
    k=16
    print(search(arr,k))
