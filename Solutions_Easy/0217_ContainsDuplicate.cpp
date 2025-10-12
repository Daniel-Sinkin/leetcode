#include <unordered_set>

// Runtime 49ms | Beats 60.10%
// Memory 89.55 MB | Beats 72.12%
class Solution {
public:
    bool containsDuplicate(vector<int> &nums) {
        std::unordered_set<int> seen;
        seen.reserve(nums.size());

        for (size_t i = 0; i < nums.size(); ++i) {
            auto [it, inserted] = seen.insert(nums[i]);
            if (!inserted) {
                return true;
            }
        }
        return false;
    }
};

// Alternatively, using STL
// Runtime 19ms | Beats 92.77%
// Memory 74.42 MB | Beast 72.86%
class Solution {
public:
    bool containsDuplicate(const std::vector<int> &a) {
        auto b = a;
        std::sort(b.begin(), b.end());
        return std::adjacent_find(b.begin(), b.end()) != b.end();
    }
};