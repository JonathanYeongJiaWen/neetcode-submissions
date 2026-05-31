class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        if len(prices) == 1:
            return 0
        b = 0 
        s = 1
        while s < len(prices):
            bp = prices[b]
            sp = prices[s]
            maxP = max(maxP,sp - bp)
            if sp < bp:
                b = s
                s = b + 1
            else:
                s += 1
        return maxP


