class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        i,c = 0,0
        while nums:
            if nums[mid] == target: return i+mid
            elif nums[mid] > target:
                nums = nums[:mid]
            else:
                nums = nums[mid+1:]
                i += mid+1
            mid = len(nums) // 2
        return -1
