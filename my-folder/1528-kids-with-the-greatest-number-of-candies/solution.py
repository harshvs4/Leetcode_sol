class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        n = len(candies)
        arr = [False]*(n)

        for i in range(n):
            if candies[i] + extraCandies >= maxi:
                arr[i] = True

        return arr
        
