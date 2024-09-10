class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n  # Initialize the result array with 1's to store the output

        # First pass: Calculate prefix products
        prefix_product = 1
        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]

        # Second pass: Calculate suffix products and multiply with the prefix products
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]

        return result

