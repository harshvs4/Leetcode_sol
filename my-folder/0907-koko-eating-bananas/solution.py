import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search range for Koko's eating speed
        low, high = 1, max(piles)
        
        # Function to check if Koko can finish all bananas at a given speed in h hours
        def canFinish(speed):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / speed)  # Calculate the number of hours for this pile
            return hours <= h
        
        # Perform binary search
        while low < high:
            mid = (low + high) // 2
            if canFinish(mid):
                high = mid  # If she can finish with speed `mid`, try a slower speed
            else:
                low = mid + 1  # Otherwise, increase the speed
        
        return low

