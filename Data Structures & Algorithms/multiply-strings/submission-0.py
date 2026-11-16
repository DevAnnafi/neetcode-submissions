class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        number1 = int(num1)
        number2 = int(num2)

        multi = number1 * number2

        return "".join(str(multi))
