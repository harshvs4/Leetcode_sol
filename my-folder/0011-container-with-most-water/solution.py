class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        mul = 1
        maxi = float('-inf')

        while i < j:
            width = j-i
            mul = min(height[i], height[j]) * width
            maxi = max(maxi, mul)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return maxi





        
