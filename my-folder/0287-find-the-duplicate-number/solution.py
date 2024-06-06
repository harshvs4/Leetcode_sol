class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = [0] * len(nums)

        for x in nums:
            if arr[x] == 1:
                return x
            arr[x]+=1
