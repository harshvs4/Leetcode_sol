class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in dict1:
                return [dict1[comp], i]
            else:
                dict1[nums[i]] = i        
