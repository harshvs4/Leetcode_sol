class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        print(citations)
        n = len(citations)
        maxi = 0

        for i in range(n):
            if citations[i] >= i+1:
                maxi = i+1
            else:
                break
        
        return maxi

        
