class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        x = len(flowerbed)
        if n == 0: 
            return True  # No need to plant any flowers

        for i in range(x):
            # Check if current spot is empty, and both neighbors (if they exist) are empty
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == x-1 or flowerbed[i+1] == 0):
                # Plant a flower
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True  # Early exit if no more flowers need to be planted

        return n == 0  # Return true if all required flowers were planted

