from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        for x in range(len(nums)):
            if nums[x] == target:
                return x
            if nums[x] > target:
                return x
            if x + 1 == len(nums):
                return x + 1





nums = [1,3,5,6]
target = 7

solution = Solution()
result = solution.searchInsert(nums,target)
print(result)