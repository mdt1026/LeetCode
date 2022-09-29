class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        d = {}
        Min = prices[0]
        p = 0
        for n in prices[1:]:
            p = max(p, n - Min)
            Min = min(Min, n)
        return p
