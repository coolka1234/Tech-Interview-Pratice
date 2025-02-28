# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
from collections import Counter
import heapq

def top_k_frequent(nums, k):
    freq_map = Counter(nums)
    return [item[0] for item in heapq.nlargest(k, freq_map.items(), key=lambda x: x[1])]


nums = [1,1,1,2,2,3]
k = 2
print(top_k_frequent(nums, k))  

