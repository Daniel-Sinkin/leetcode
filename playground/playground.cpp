#include <algorithm>
#include <bitset>
#include <iostream>
#include <print>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>

using std::print, std::println;

auto main() -> int {
    std::unordered_set<int> set(nums.begin(), nums.end());
    int best = 0;

    for (int n : set) {
        bool is_start_of_sequence = (set.count(n - 1) == 0);
        if (is_start_of_sequence) {
            int cur = n;
            int length = 1;

            while (set.count(cur + 1)) {
                cur += 1;
                length += 1;
            }

            best = std::max(best, length);
        }
    }
    return best;

    set.insert(5);
    set.insert(6);
    set.insert(7);
    set.insert(9);

    for (int x : set) {
        std::println("{}", x);
    }
}