class Solution:
    def rob(self, nums: List[int]) -> int:
        m = {}
        def r(n):
            if n < 0: 
                return 0
            if n in m:
                return m[n]

            result = max(nums[n] + r(n-2), r(n-1))
            m[n] = result
            return result
        return r(len(nums)-1)
