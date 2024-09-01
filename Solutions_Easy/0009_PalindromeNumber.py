class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True

        x_tmp = x
        n_digits = 0
        while x_tmp > 0:
            x_tmp = x_tmp // 10
            n_digits += 1

        digits = []
        for i in range(n_digits // 2):
            digits.append(x % 10)
            x = x // 10

        # If we have odd digits we can skip the digit in the middle
        if n_digits & 1 == 1:
            x = x // 10

        for i in range(n_digits // 2):
            if x % 10 != digits[-(i + 1)]:
                return False
            x = x // 10

        return True
