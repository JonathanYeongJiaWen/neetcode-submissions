class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        l, r = 0, 1
        store = s[l]
        maxL = 1
        while r < len(s):
            if s[r] not in store:
                store += s[r]
            else:
                maxL = max(maxL, len(store))
                store = store[store.index(s[r])+1:] + s[r]
            r += 1
        return max(maxL, len(store))




