class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = m = 0

        for i in nums:
            if i == 1:
                count+=1
                m = max(m, count)
            else:
                count = 0
        return m
        
