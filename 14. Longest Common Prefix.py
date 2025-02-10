from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = strs[0]

        for x in strs[1:]:
            while not x.startswith(prefix):
                prefix = prefix[:-1]

            if not prefix:
                return ""

        return prefix



strs = ["teste", "teta", "tenta"]
solution = Solution()
result = solution.longestCommonPrefix(strs)
print(result)