class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        int s_list[26] = {0};
        int t_list[26] = {0};

        for (size_t i = 0; i < s.length(); ++i) {
            s_list[s[i] - 'a'] += 1;
            t_list[t[i] - 'a'] += 1;
        }

        for (size_t i = 0; i < 26; ++i) {
            if (s_list[i] != t_list[i]) {
                return false;
            }
        }

        return true;
    }
};