class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        lstr = []

        i = 0
        n = len(nums)

        while i < n:
            j = i
            # Move j forward while nums[j] and nums[j + 1] are consecutive
            while j + 1 < n and nums[j + 1] == nums[j] + 1:
                j += 1
            
            # If j moved, we have a range
            if i != j:
                lstr.append("{}->{}".format(nums[i], nums[j]))
            else:
                # Single element, no range
                lstr.append("{}".format(nums[i]))

            # Move i to the next possible start of a range
            i = j + 1

        return lstr

