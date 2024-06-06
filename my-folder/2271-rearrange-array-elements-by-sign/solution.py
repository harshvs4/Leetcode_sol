class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = 0, 1
        n = len(nums)
        a = [0]* n
        for i in range(len(nums)):
            if nums[i] < 0:
                a[neg] = nums[i]
                neg+=2
            if nums[i] >= 0:
                a[pos] = nums[i]
                pos+=2
        return a
        
