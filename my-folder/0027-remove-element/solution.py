class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = j = len(nums)-1

        while i >= 0:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                i-=1
                j-=1
            else:
                i-=1
        
        return j+1
        
