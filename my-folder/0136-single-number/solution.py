class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict1 = {}

        for i in nums:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        return min(dict1, key = dict1.get)
        
