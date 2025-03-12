from time import process_time


class Solution:
    def mySqrt(self, x: int) -> int:

        # array = []
        # aux = 2
        # raiz = 1
        #
        # while x > 1:
        #     if x % aux == 0:
        #         x = x / aux
        #         array.append(aux)
        #     else:
        #         aux += 1
        #
        # if len(array) > 2:
        #     for y in range(len(array)):
        #         if len(array) > 1:
        #             if array[y] == array[y+1]:
        #                 raiz *= array[y]
        #
        #
        #
        # return array
        # return raiz

        elevado = 1

        if x == 0:
            return 0

        for i in range(x):

            if elevado * elevado == x:
                return elevado
            if elevado * elevado < x and (elevado + 1) * (elevado + 1) > x:
                return elevado

            elevado += 1

        return elevado








x = 14
solution = Solution()
result = solution.mySqrt(x)
print(result)