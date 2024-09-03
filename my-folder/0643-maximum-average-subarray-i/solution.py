class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        sum1 = 0
        maxi = float('-inf')

        for right in range(len(nums)):
            sum1 += nums[right]
            if right - left + 1 == k:
                avg = sum1/k
                maxi = max(maxi, avg)
                sum1 -= nums[left]
                left+=1
            
            

        return maxi
            
        
