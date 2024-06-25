class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(arr):
            if len(arr) <= 1:
                return 0  # Base case: no inversions in a single-element array
            
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            
            # Recursively sort both halves and count inversions in them
            count_left = merge_sort(left)
            count_right = merge_sort(right)
            
            # Merge the two halves and count split inversions
            count_split = merge_two_sorted(left, right, arr)
            
            # Total inversions is sum of inversions in left half, right half, and split inversions
            return count_left + count_right + count_split

        def merge_two_sorted(a, b, arr):
            len_a = len(a)
            len_b = len(b)
            
            i = j = k = 0
            count = 0
            
            # Merge process
            while i < len_a and j < len_b:
                if a[i] <= b[j]:
                    arr[k] = a[i]
                    i += 1
                else:
                    arr[k] = b[j]
                    j += 1
                k += 1
            
            # Copy remaining elements of a, if any
            while i < len_a:
                arr[k] = a[i]
                i += 1
                k += 1
            
            # Copy remaining elements of b, if any
            while j < len_b:
                arr[k] = b[j]
                j += 1
                k += 1
            
            # Count specific pairs where x[p] > 2 * y[q]
            j = 0
            for p in range(len_a):
                while j < len_b and a[p] > 2 * b[j]:
                    j += 1
                count += j
            
            return count
        count = merge_sort(nums)
        return count
        
