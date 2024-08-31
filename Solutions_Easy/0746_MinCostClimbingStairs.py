class Solution:
    def _min_cost_climbing_stairs(self, i: int) -> int:
        if i < 0:
            return 0

        if self.cost_total[i] == -1:
            self.cost_total[i] = min(
                self.cost[i - 1] + self._min_cost_climbing_stairs(i - 1),
                self.cost[i - 2] + self._min_cost_climbing_stairs(i - 2),
            )

        return self.cost_total[i]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = cost
        self.cost_total = [0, 0] + [-1] * (len(cost) - 2)

        n = len(cost)
        self._min_cost_climbing_stairs(n - 1)
        return min(
            self.cost[-1] + self.cost_total[-1], self.cost[-2] + self.cost_total[-2]
        )
