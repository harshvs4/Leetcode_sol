class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = set(nums1)
        y = set(nums2)
        res = []

        for i in x:
            if i in y:
                res.append(i)

        return res
        
