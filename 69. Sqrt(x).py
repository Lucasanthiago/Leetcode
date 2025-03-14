from time import process_time


class Solution:
    def mySqrt(self, x: int) -> int:


        # maneira fudida que eu fiz
        # elevado = 1
        #
        # if x == 0:
        #     return 0
        #
        # for i in range(x):
        #
        #     if elevado * elevado == x:
        #         return elevado
        #     if elevado * elevado < x and (elevado + 1) * (elevado + 1) > x:
        #         return elevado
        #
        #     elevado += 1
        #
        # return elevado


        # outra maneira idiota
        #
        # i = 0
        #
        # while True:
        #     if i * i == x:
        #         return i
        #     if i * i > x:
        #         return i-1
        #     else:
        #         i += 1

        l, r = 0, x
        res = 0

        while l <= r:
            m = l + ((r-l) // 2)
            if m*m > x:
                r = m -1
            elif m*m < x:
                l = m + 1
                res = m
            else:
                return m
        return res








x = 14
solution = Solution()
result = solution.mySqrt(x)
print(result)