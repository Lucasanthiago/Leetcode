from operator import index


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:


        # for x in range(len(needle)):
        #     if needle[x] != haystack[x]:
        #         return -1
        #
        # return 0
        # aux = ""
        # auxCount = 0
        # indexSave = 0
        #
        # for x in range(len(haystack)):
        #     if haystack[x] == needle[auxCount] and auxCount:
        #         aux += haystack[x]
        #         auxCount += 1
        #         indexSave = x
        #     else:
        #         if aux == needle:
        #             indexSave = indexSave - len(needle) - 1
        #             if indexSave < 0:
        #                 return 0
        #             else:
        #                 return indexSave
        #         else:
        #             aux = ""
        #             auxCount = 0
        # return -1

        if needle == "":
            return 0

        if len(haystack) < len(needle):
            return -1


        for x in range(len(haystack) - len(needle) + 1):
            for y in range(len(needle)):
                if haystack[y + x] != needle[y]:
                    break
                if y == len(needle) - 1:
                    return x
        return -1



haystack = "sticksadstick"
needle = "sad"

solution = Solution()
result = solution.strStr(haystack, needle)
print(result)