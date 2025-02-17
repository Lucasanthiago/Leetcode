from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1

        for x in range(1, len(nums)):
            if nums[x] != nums[x-1]:
                nums[k] = nums[x]
                k += 1
        return k

#chek again after
class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        for i in range(1, len(nums)):
            if nums[index-1] == nums[i]:
                continue
            else:
                nums[index] = nums[i]
                index += 1
        return index




# Teste
nums = [1,1,2]
solution = Solution()
result = solution.removeDuplicates(nums)
print(result)  # Deve retornar (3, [1, 2, 3])
