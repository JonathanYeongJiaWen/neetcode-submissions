class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxW = 0
        maxLH = heights[l]
        maxRH = heights[r]
        while l<r:
            curW = min(maxLH,maxRH) * (r-l)
            maxW = max(maxW,curW)
            if heights[l] < heights[r]:
                l+=1
                maxLH = max(maxLH, heights[l])
            else:
                r-=1
                maxRH = max(maxRH, heights[r])

            
        return maxW


