class Solution:
    def _climb_stairs(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if self.memoized[n - 1] == -1:
            self.memoized[n - 1] = self._climb_stairs(n - 1) + self._climb_stairs(n - 2)

        return self.memoized[n - 1]

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        self.memoized = [1, 2] + [-1] * (n - 2)

        return self._climb_stairs(n)
