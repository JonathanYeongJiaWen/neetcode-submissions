class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        window = ''
        maxL = 0
        for char in s:
            if char in window:
                window = window[window.index(char)+1:]
            window += char
            maxL = max(maxL,len(window))
        return maxL



        