# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
def find_sum(array, target):
    scores={}
    i=0
    for i, num in enumerate(array):
        complement=target-num
        if complement in scores:
            return scores[complement], i
        else:
            scores[num]=i
    return []
    

if __name__=="__main__":
    array=[3,2,4]
    target=6
    print(find_sum(array, target))
