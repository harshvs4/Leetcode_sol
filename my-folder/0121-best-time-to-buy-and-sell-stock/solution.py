class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            p = prices[i] - buy

            if buy > prices[i]:
                buy = prices[i]
            else:
                profit = max(p, profit)

        return profit

        
