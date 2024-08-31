class Solution {
public:
    int maxProfit(const std::vector<int> &prices) {
        if (prices.size() == 1) {
            return 0;
        }

        int cum_max_val = -1;
        std::vector<int> cum_max_list(prices.size(), cum_max_val);

        for (int i = prices.size() - 1; i >= 0; --i) {
            cum_max_val = (prices[i] > cum_max_val) ? prices[i] : cum_max_val;
            cum_max_list[i] = cum_max_val;
        }

        int max_profit = 0;
        for (size_t i = 0; i < prices.size() - 1; ++i) {
            int profit = cum_max_list[i + 1] - prices[i];
            max_profit = (profit > max_profit) ? profit : max_profit;
        }

        return max_profit > 0 ? max_profit : 0;
    }
};
