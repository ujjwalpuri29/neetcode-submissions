class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestBuy, bestProfit = float('inf'), 0
        for i in range(len(prices)):
            bestBuy = min(bestBuy, prices[i])
            profit = prices[i] - bestBuy
            bestProfit = max(bestProfit, profit)
        return bestProfit