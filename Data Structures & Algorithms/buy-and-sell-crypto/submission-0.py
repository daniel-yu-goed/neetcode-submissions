class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: # no future day for selling
            return 0

        priceMin = prices[0]
        profitMax = 0

        for i in range(len(prices)):
            priceMin = min(priceMin, prices[i])
            profitMax = max(profitMax, prices[i] - priceMin)

        return profitMax

            
        