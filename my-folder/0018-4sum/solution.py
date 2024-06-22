class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            if i!=0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                x = j+1
                y = n-1

                while x < y:
                    total = nums[i]+nums[j]+nums[x]+nums[y]
                    if total < target:
                        x+=1
                    elif total > target:
                        y-=1
                    else:
                        ans.append([nums[i],nums[j],nums[x],nums[y]])
                        x+=1
                        y-=1
                        while x < y and nums[x] == nums[x-1]:
                            x+=1
                        while x < y and nums[y] == nums[y+1]:
                            y-=1
                    
        return ans
        
