#krl vai tomar no cu facil eh o krl

class Solution:
    def isValid(self, s: str) -> bool:

        close_open = {
            ')':'(',
            ']':'[',
            '}':'{',
        }

        stack = []

        for letra in s:
            if letra in close_open:
                if stack and stack[-1] == close_open[letra]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(letra)

        if stack:
            return False
        if not stack:
            return True

