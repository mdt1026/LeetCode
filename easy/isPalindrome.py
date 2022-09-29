class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ""
        for c in s.lower():
            if c.isalnum(): tmp += c
        s = tmp
        
        while len(s) > 1:
            if s[0] == s[-1]:
                s = s[1:-1]
            else: return False
        return True
