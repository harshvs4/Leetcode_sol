from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Sort the potions to perform binary search
        potions.sort()
        result = []
        m = len(potions)

        for spell in spells:
            # Find the minimum potion strength that forms a successful pair with the current spell
            target = success / spell
            
            # Use binary search to find the first potion that meets or exceeds the target
            idx = bisect_left(potions, target)
            
            # The number of successful pairs for this spell is the number of potions from idx to the end
            result.append(m - idx)

        return result

