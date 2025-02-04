
#1 Solution(very bad)
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range (len(nums)):
            for y in range (len(nums)):
                if nums[i] + nums[y] == target and i != y:
                    return [i, y]


#2 Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                if nums[x] + nums[y] == target:
                    return [x,y]


#3 Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


