from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort_and_count(nums, start, end):
            if start >= end:
                return 0

            mid = (start + end) // 2
            count = 0

            # Count in left half, right half, and across the halves
            count += merge_sort_and_count(nums, start, mid)
            count += merge_sort_and_count(nums, mid + 1, end)

            # Count reverse pairs across the two halves
            j = mid + 1
            for i in range(start, mid + 1):
                while j <= end and nums[i] > 2 * nums[j]:
                    j += 1
                count += (j - (mid + 1))

            # Merge the two halves
            merge(nums, start, mid, end)

            return count

        def merge(nums, start, mid, end):
            # Temporary array to hold the merged result
            temp = []
            i, j = start, mid + 1

            # Merge the two sorted halves
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1

            # Copy the remaining elements
            while i <= mid:
                temp.append(nums[i])
                i += 1

            while j <= end:
                temp.append(nums[j])
                j += 1

            # Copy the sorted subarray back into the original array
            for i in range(len(temp)):
                nums[start + i] = temp[i]

        return merge_sort_and_count(nums, 0, len(nums) - 1)



