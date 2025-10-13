#include <array>
#include <unordered_map>

template <class T, std::size_T N>
struct ArrayHash {
    size_t operator()(const std::array<T, N> &arr) const noexcept {
        size_t h = 0;
        for (const T &x : arr) {
            h = h * 31 + std::hash<T>{}(x);
        }
        return h;
    }
};

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string> &strs) {
        std::vector<std::vector<string>> retval{};
        std::unordered_map<std::array<int, 26>, size_t, ArrayHash> my_map;

        for (const string &word : strs) {
            std::array<int, 26> arr{};
            for (char c : word) {
                ++arr[c - 'a'];
            }
            auto search = my_map.find(arr);
            bool found_entry = search != my_map.end();
            if (found_entry) {
                retval[search->second].push_back(word);
            } else {
                retval.emplace_back(1, word);
                my_map[arr] = retval.size() - 1;
            }
        }
        return retval;
    }
};