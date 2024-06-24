"""https://leetcode.com/problems/multiply-strings/description/"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_: list[int] = [int(n1) for n1 in num1][::-1]
        num2_: list[int] = [int(n2) for n2 in num2][::-1]

        total: int = 0
        for i, x in enumerate(num1_):
            for j, y in enumerate(num2_):
                total += x * y * 10 ** (i + j)
        return str(total)
