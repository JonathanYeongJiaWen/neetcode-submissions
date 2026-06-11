class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        word = ''
        for char in s:
            if char.isalnum():
                word += char
        l = 0
        r = len(word) - 1
        while l<=r:
            if word[l] == word[r]:
                l+=1
                r-=1
            else:
                return False
        return True