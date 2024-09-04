#include <algorithm> // for std::max_element and std::max

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int> &nums, int k) {
        vector<int> retval = {};
        size_t max_idx = 0;
        int max_val = -100000; // -10^4 <= nums[i] <= 10^4
        for (int i = 0; i < k; i++) {
            if (nums[i] >= max_val) {
                max_idx = i;
                max_val = nums[i];
            }
        }
        retval.push_back(max_val) for (int i = 0; i < nums.size() - k; i++) {
            if (nums[i] < max_val) {
                if (nums[i + k] >= max_val) {
                    max_idx = i + k;
                    max_val = nums[i + k];
                }
            } else if (i == max_index) {
                max_index = i;
                max_val = nums[i];
            } else {
            }
        }
    }
};