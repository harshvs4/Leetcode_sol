class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        arr1 = []

        for i in nums1:
            if i not in nums2:
                arr1.append(i)

        arr2 = []

        for i in nums2:
            if i not in nums1:
                arr2.append(i)
        
        arr = []
        arr.append(set(arr1))
        arr.append(set(arr2))

        return arr
