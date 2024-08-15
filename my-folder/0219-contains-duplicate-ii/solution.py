class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ddict = {}

        for i in range(len(nums)):
            if nums[i] in ddict:
                if abs(ddict[nums[i]] - i) <= k:
                    return True
            
            ddict[nums[i]] = i

        return False
        
