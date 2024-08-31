class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        cum_max_val = -1
        cum_max_list = [cum_max_val] * len(prices)
        for i, x in enumerate(prices[::-1]):
            if x > cum_max_val:
                cum_max_val = x
            cum_max_list[len(prices) - i - 1] = cum_max_val

        max_profit_list = []
        for i, price in enumerate(prices[:-1]):
            max_profit_list.append(-price + cum_max_list[i + 1])

        return max(0, max(max_profit_list))
