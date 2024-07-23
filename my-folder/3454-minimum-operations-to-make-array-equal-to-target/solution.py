class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)
        diff = [0]*n
        for i in range(n):
            diff[i] = target[i] - nums[i]
            
        ans = incOp = decOp = 0

        for i in range(n):
            if diff[i] > 0:
                if incOp < diff[i]:
                    extra = diff[i] - incOp
                    ans += extra
                incOp = diff[i]
                decOp = 0

            elif diff[i] < 0:
                if decOp < -diff[i]:
                    extra = -diff[i] - decOp
                    ans += extra
                decOp = -diff[i]
                incOp = 0
            else:
                incOp = decOp = 0

        return ans 
        
