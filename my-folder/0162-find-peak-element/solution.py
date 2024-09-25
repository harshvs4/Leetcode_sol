class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def binary_search(low, high):
            if low == high:
                return low  # If there's only one element, that's the peak
            
            mid = (low + high) // 2
            
            # Check if mid is greater than the next element
            if nums[mid] > nums[mid + 1]:
                # Search left part of the array (mid could be the peak)
                return binary_search(low, mid)
            else:
                # Search right part of the array
                return binary_search(mid + 1, high)

        return binary_search(0, len(nums) - 1)

