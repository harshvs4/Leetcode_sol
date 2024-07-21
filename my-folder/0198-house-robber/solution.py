class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = nums[0]
        prev2 = 0
        for i in range(1, len(nums)):
            notPick = 0 + prev
            pick = nums[i] + prev2
            curr = max(pick, notPick)
            prev2 = prev
            prev = curr
        return prev
        
