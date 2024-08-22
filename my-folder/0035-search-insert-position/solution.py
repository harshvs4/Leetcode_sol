class Solution:
    def search(self, nums, start, end, target):
        if start > end:
            return start  # Return the insertion point if target is not found

        mid = (start + end) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.search(nums, mid + 1, end, target)  # Search in the right half
        else:
            return self.search(nums, start, mid - 1, target)  # Search in the left half

    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0
        end = n - 1

        return self.search(nums, start, end, target)

