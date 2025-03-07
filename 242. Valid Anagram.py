from collections import Counter


class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


solution = Solution()
result = solution.isAnagram(s="jar", t="jra")
print(result)
