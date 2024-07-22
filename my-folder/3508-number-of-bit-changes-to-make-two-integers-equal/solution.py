class Solution:
    def minChanges(self, n: int, k: int) -> int:
        xor_val = n ^ k
        
        # Check if there are bits that are 1 in k and 0 in n
        if (k & ~n) != 0:
            return -1  # Impossible to convert
        
        # Count the number of 1 bits in n that need to be turned to 0
        count = 0
        while xor_val:
            if (xor_val & 1) and (n & 1):
                count += 1
            xor_val >>= 1
            n >>= 1
        
        return count
        
