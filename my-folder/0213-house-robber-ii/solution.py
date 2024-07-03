class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob2(nums):
            m = {}
            def r(n):
                if n < 0:
                    return 0 
                if n in m:
                    return m[n]

                result= max(nums[n]+r(n-2), r(n-1))
                m[n] = result
                return result
            return r(len(nums)-1)
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        p = rob2(nums[1:])
        q = rob2(nums[:-1])
        return max(p,q)
