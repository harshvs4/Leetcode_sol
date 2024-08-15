class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ddict = {}

        for i in range(len(nums)):
            x = target - nums[i]
            if x in ddict:
                return [i, ddict[x]]
            else:
                ddict[nums[i]] = i

        return [-1,-1]
        
