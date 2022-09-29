class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            n = nums[i]
            diff = target - n
            if diff in d:
                return [i, d[diff]]
            d[n] = i
                
