from typing import List
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    res=[]
    i=0
    j=0
    k=0
    while i < m+n and j < n:
        if nums1[i]<=nums2[j] and nums1[i]>0:
            res.insert(k, nums1[i])
            i+=1
        else:
            res.insert(k, nums2[j])
            j+=1
        k+=1
    print(res)

if __name__ == '__main__':
    merge([1,2,3,0,0,0],3,[2,5,6],3)