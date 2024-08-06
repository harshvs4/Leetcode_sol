class Solution:
    def lrotate(self, nums, start, end):
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        k = k%n
        self.lrotate(nums, 0, n-1)
        self.lrotate(nums, 0, k-1)
        self.lrotate(nums, k, n-1)
        
