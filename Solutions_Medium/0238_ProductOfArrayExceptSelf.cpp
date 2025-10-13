class Solution {
public:
    vector<int> productExceptSelf(vector<int> &nums) {
        std::vector<int> retval{};
        retval.resize(nums.size(), 1);

        int left_to_right = 1;
        int right_to_left = 1;
        for (size_t left_idx = 0; left_idx < nums.size(); ++left_idx) {
            size_t right_idx = nums.size() - left_idx - 1;

            retval[left_idx] *= left_to_right;
            retval[right_idx] *= right_to_left;

            left_to_right *= nums[left_idx];
            right_to_left *= nums[right_idx];
        }
        return retval;
    }
};