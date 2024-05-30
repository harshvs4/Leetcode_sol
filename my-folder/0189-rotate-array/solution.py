class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        def swap(x,y,nums):
            temp = nums[x]
            nums[x] = nums[y]
            nums[y] = temp
        
        def lrotate(start, end, nums):
            while start <= end:
                swap(start, end, nums)
                start+=1
                end-=1

        lrotate(0,n-1, nums)
        lrotate(0,k-1,nums)
        lrotate(k, n-1, nums)
        
