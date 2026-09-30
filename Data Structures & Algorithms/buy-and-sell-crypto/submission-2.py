class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## Time complexity: O(n)
        ## Space complexity: O(1)
        ## 
        ## Dynamic programming approach
        ## Track:
        # 1. The lowest price so far → this is the best day to buy.
        # 2. The best profit so far → selling today minus the lowest buy price seen earlier.
        
        priceMin = prices[0]
        profitMax = 0

        for i in range(len(prices)):
            priceMin = min(priceMin, prices[i])
            profitMax = max(profitMax, prices[i] - priceMin)

        return profitMax

            
        