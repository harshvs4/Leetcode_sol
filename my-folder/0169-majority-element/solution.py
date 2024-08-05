class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        cnt = 0

        for i in range(len(nums)):
            if cnt == 0:
                candidate = nums[i]
                cnt += 1
            elif candidate == nums[i]:
                cnt += 1
            else:
                cnt -= 1
        
        return candidate
        
