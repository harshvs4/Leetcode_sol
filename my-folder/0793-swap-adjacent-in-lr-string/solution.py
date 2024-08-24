class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        i, j = 0, 0
        n = len(start)
        
        while i < n or j < n:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X':
                j += 1
            
            if (i < n) != (j < n):
                return False  # One of them reached the end but the other did not
            
            if i < n and j < n:
                if start[i] != end[j]:
                    return False  # Different characters
                
                if start[i] == 'L' and i < j:
                    return False  # 'L' in start moved to the right
                if start[i] == 'R' and i > j:
                    return False  # 'R' in start moved to the left
            
            i += 1
            j += 1
        
        return True
