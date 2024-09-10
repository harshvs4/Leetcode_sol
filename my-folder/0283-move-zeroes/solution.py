class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = 0  # This pointer will track the position to place the next non-zero element.

        # Traverse through the list.
        for i in range(n):
            if nums[i] != 0:
                # Swap the non-zero element with the element at index `j`.
                nums[i], nums[j] = nums[j], nums[i]
                j += 1  # Move `j` to the next position for non-zero elements.

