from traceback import print_tb
from typing import List



class Solution:
    def lengthOfLastWord(self, s: str) -> int:



        for i in range(len(s)):
            if s.endswith(" "):
                s = s[:-1]
            else:
                break

        if len(s) == 1 and s[0] != ' ':
            return 1

        k = 0
        vemDeTras = len(s) - 1


        for x in range(len(s)):
            if s[vemDeTras - x] == " ":
                return k
            k += 1

        return k

s = "day"
solution = Solution()
result = solution.lengthOfLastWord(s)
print(result)