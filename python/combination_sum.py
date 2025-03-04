# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
#
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
#
# of at least one of the chosen numbers is different.
#
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
#
def combinations(array, target):
    results=[float("inf")]*(target+1)
    results[0]=0
    for elem in array:
        for i in range(elem, target+1):
            results[i]=min(results[i], results[i-elem]+1)
    return filter(lambda x: x!=float("inf"), results)

array=[2,3,6,7]
target=9
result=combinations(array, target)
for x in result:
    print(x)

