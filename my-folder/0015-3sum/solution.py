from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int, start: int) -> List[List[int]]:
        # Two-pointer technique to find two numbers that sum to the target
        results = []
        dict1 = {}

        for i in range(start, len(nums)):
            comp = target - nums[i]
            if comp in dict1:
                results.append([comp, nums[i]])
            dict1[nums[i]] = i
        
        return results

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array to use the two-pointer technique
        res = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates

            target = -nums[i]
            two_sum_results = self.twoSum(nums, target, i + 1)

            for pair in two_sum_results:
                triplet = [nums[i]] + pair
                res.append(triplet)

        # To remove potential duplicates:
        return list(set(map(tuple, res)))


