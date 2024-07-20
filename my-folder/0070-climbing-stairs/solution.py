class Solution:
    def climbStairs(self, n: int) -> int:
        prev = prev2 = 1
        
        if n == 1:
            return 1
        
        curr = 0
        for i in range(2, n+1):
            curr = prev+prev2
            prev2 = prev
            prev = curr
        
        return curr
        
