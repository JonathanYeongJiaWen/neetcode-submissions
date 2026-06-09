import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        mink = r
        while l<=r:
            mid = (l+r)//2
            totalH = 0
            for banana in piles:
                totalH += math.ceil(float(banana)/mid)
            if totalH <= h:
                mink = min(mink,mid)
                r = mid-1
            else:
                l = mid + 1
        return mink
            

