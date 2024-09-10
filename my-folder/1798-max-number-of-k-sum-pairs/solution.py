class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        dict1 = {}

        # Iterate through the array once
        for i in nums:
            target = k - i

            # Check if target (complementary number) exists in dict1 and has non-zero count
            if target in dict1 and dict1[target] > 0:
                count += 1  # Found a valid pair
                dict1[target] -= 1  # Reduce count for the target since it's used in the pair
            else:
                # Add the current number to dict1 (or increment its count)
                if i in dict1:
                    dict1[i] += 1
                else:
                    dict1[i] = 1

        return count

