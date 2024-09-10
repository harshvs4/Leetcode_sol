class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = float('-inf')

        i = 0
        j = len(height)-1

        while i < j:
            maxi = max(maxi, min(height[i], height[j])*(j-i))

            if height[i] <= height[j]:
                i+=1
            else:
                j-=1

        return maxi

        
