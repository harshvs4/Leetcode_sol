class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        prefix = [0]*n
        suffix = [0]*n
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]

        for i in range(1, n):
            prefix[i] += nums[i] + prefix[i-1]

        #print(prefix)

        for i in range(n-2, -1,-1):
            suffix[i] += nums[i] + suffix[i+1]

        #print(suffix)
        for i in range(n):
            if i == 0:
                if suffix[i+1] == 0:return 0
            elif i == n-1:
                if prefix[i-1] == 0:return n-1
            elif prefix[i-1] == suffix[i+1]:
                return i

        return -1
        
