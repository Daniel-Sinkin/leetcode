class Solution {
private:
    vector<int> cost_total;
    vector<int> cost;

    int _min_cost_climbing_stairs(int i) {
        if (i < 0) {
            return 0;
        }

        if (cost_total[i] == -1) {
            int min_cost = (cost[i - 1] + _min_cost_climbing_stairs(i - 1) < cost[i - 2] + _min_cost_climbing_stairs(i - 2))
                               ? cost[i - 1] + _min_cost_climbing_stairs(i - 1)
                               : cost[i - 2] + _min_cost_climbing_stairs(i - 2);

            cost_total[i] = min_cost;
        }

        return cost_total[i];
    }

public:
    int minCostClimbingStairs(vector<int> &cost) {
        this->cost = cost;
        cost_total = vector<int>(2, 0);     // Initialize the first two elements with 0
        cost_total.resize(cost.size(), -1); // Resize and initialize remaining elements with -1

        int n = cost.size();
        _min_cost_climbing_stairs(n - 1);
        return (cost[n - 1] + cost_total[n - 1] < cost[n - 2] + cost_total[n - 2])
                   ? cost[n - 1] + cost_total[n - 1]
                   : cost[n - 2] + cost_total[n - 2];
    }
};