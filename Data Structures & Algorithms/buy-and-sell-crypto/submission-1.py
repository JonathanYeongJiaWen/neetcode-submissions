class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        l= 0
        r= 1
        lowest = prices[l]
        maxP = 0
        while r < len(prices):
            profit = prices[r] - lowest
            maxP = max(maxP, profit)
            if prices[r] < lowest:
                lowest = prices[r]
                l = r 
            r+=1
        return maxP
        
            

        