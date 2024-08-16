class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # Only check if `num` is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Check for the next consecutive numbers in the sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

