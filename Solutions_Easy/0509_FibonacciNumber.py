class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        i = 2

        fib0 = 1
        fib1 = 1
        fib2 = 0

        while i < n:
            fib2 = fib1
            fib1 = fib0
            fib0 = fib1 + fib2
            i += 1

        return fib0
