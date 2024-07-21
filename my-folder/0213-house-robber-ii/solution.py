class Solution:
    def pick(self, nums: List[int]) -> int:
        prev = nums[0]
        prev2 = 0
        for i in range(1, len(nums)):
            notPick = 0 + prev
            pick = nums[i] + prev2
            curr = max(pick, notPick)
            prev2 = prev
            prev = curr
        return prev

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:return nums[0]
        x = nums[:-1]
        y = nums[1:]

        return max(self.pick(x), self.pick(y))
