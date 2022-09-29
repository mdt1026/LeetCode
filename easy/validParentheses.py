class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c in d:
                stack.append(c)
            elif not stack:
                return False
            else:
                left = stack.pop()
                if not c == d[left]:
                    return False
        return not stack
