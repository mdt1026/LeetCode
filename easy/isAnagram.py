class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        d = {}
        for c in s:
            if not d.get(c, None):
                d[c] = 1
            else: d[c] += 1
        for c in t:
            if not d.get(c, None):
                return False
            else:
                d[c] -= 1
            if d[c] == 0:
                d.pop(c)
        return not d
        """
        d1,d2 = {},{}
        for c in s:
            d1[c] = d1.get(c,0)+1
        for c in t:
            d2[c] = d2.get(c,0)+1
        return d1 == d2
