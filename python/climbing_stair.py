# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
#
#
# Example 1:
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
global result


def ways_to_climb(n):
    result=0
    def climb(result, n, counter):
        print(counter)
        if counter+1==n:
            result+=1
            print("found")
            return
        climb(result, n, counter+1)
        if counter+2==n:
            result+=1
            print("found")
            return
        climb(result, n, counter+2)
    counter=0
    climb(result, n, counter)
    return result

def ways_to_climb_2(n):
    def climb(counter):
        if counter == n:
            return 1  
        if counter > n:
            return 0  
        return climb(counter + 1) + climb(counter + 2)  
    return climb(0)


n = 5
print(ways_to_climb(n))  # Output: 8

n=5
print(ways_to_climb(n))

