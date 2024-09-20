class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        
        while low <= high:
            mid = (low + high) // 2
            result = guess(mid)
            
            if result == 0:
                return mid  # Found the number
            elif result == -1:
                high = mid - 1  # The target number is smaller
            else:
                low = mid + 1  # The target number is larger
                
        return -1  # This line is just a fallback, the function should always return within the loop

