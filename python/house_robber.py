# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

def rob_houses(array):
    sum_1, sum_2=0, 0
    num_of_houses=len(array)
    for i in range(num_of_houses):
        if(i%2==0):
            sum_2+=array[i]
        else:
            sum_1+=array[i]
    return max(sum_1, sum_2)


def rob_houses_2(nums):
    prev, curr = 0, 0  

    for num in nums:
        prev, curr = curr, max(curr, prev + num)

    return curr
nums = [1,2,3,1]
nums = [2,7,9,3,1]
print(rob_houses(nums))

        

