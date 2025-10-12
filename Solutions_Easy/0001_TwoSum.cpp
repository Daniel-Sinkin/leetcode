#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        std::unordered_map<int, int> seens;
        seens.reserve(nums.size());
        std::vector<int> retval{-1, -1};
        for (int i = 0; i < nums.size(); ++i) {
            auto search = seens.find(nums[i]);
            bool found_num = search != seens.end();
            if (found_num) {
                retval[0] = seens.at(nums[i]);
                retval[1] = i;
                return retval;
            } else {
                // We are looking for a m such that n + m = t <=> m = t - n
                seens.insert({target - nums[i], i});
            }
        }
        return retval;
    }
};