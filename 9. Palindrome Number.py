

class Solution1:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        num_invertido = num[::-1]
        if num == num_invertido:
            return True
        else:
            return False


class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        div = 1
        while x >= div * 10:
            div = div * 10

        while x:
            last = x % 10
            first = x // div

            if first != last:
                return False

            x = ( x % div ) // 10
            div = div / 100

        return True


class Solution3:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_num = 0
        temp = x

        while temp != 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10

        return reversed_num == x





solution = Solution3()
print(solution.isPalindrome(1221))