#include <cstddef> // For size_t
#include <limits>  // For std::numeric_limits
#include <vector>  // For std::vector

/*
Important test case
nums=
[66307295,441787703,589039035,322281864]
k=
900900704
multiplier=
641725
*/

const int MOD = 1000000007;

class Solution {
public:
    struct ModularValue {
        // For every positive integer x we can write
        // x = MOD * kx + xp where kx is a nonnegative integer and xp is an integer in [0, MOD)

        int kx;
        int xp;

        ModularValue(int xp, int kx = 0) : kx(kx), xp(xp) {}

        void multiply(int multiplier) {
            long long product = static_cast<long long>(this->xp) * multiplier;
            this->kx += product / MOD;
            this->xp = product % MOD;
        }

        long long value() const {
            return static_cast<long long>(kx) * MOD + xp;
        }

        bool operator<=(const ModularValue &other) const {
            if (this->kx < other.kx)
                return true;
            if (this->kx > other.kx)
                return false;
            return this->xp <= other.xp;
        }

        bool operator<(const ModularValue &other) const {
            if (this->kx < other.kx)
                return true;
            if (this->kx > other.kx)
                return false;
            return this->xp < other.xp;
        }

        static constexpr ModularValue maxModularValue() {
            return ModularValue(MOD - 1, std::numeric_limits<int>::max());
        }
    };

    static bool isLessOrEqual(const ModularValue &a, const ModularValue &b) {
        return a <= b;
    }

    vector<int> getFinalState(vector<int> &nums, int k, int multiplier) {
        vector<ModularValue> trackedNums;

        // emplace_back is faster because it pushes args into constructor and into vector directly without
        // creating and then later discarding a temporary value.
        // https://cplusplus.com/reference/vector/vector/emplace_back/
        for (int num : nums) {
            trackedNums.emplace_back(num);
        }

        const ModularValue max_value = maxModularValue();
        const size_t n = nums.size();

        for (size_t j = 0; j < k; j++) {
            size_t min_idx = -1;
            ModularValue min_val = max_value;
            for (size_t i = 0; i < n; i++) {
                if (trackedNums[i] < min_val) {
                    min_idx = i;
                    min_val = trackedNums[i];
                }
            }
            trackedNums[min_idx].multiply(multiplier);
        }

        return nums;
    }
};