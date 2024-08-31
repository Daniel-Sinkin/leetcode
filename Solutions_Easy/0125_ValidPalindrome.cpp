class Solution {
public:
    bool isPalindrome(std::string s) {
        std::string cleaned;
        for (char c : s) {
            if (isalnum(c)) {          // Filter non-alphanumeric chars
                cleaned += tolower(c); // Palindrome doesn't care about upper/lowercase difference
            }
        }

        int n = cleaned.size();
        for (int i = 0; i < n / 2; ++i) {
            if (cleaned[i] != cleaned[n - 1 - i]) {
                return false;
            }
        }

        return true;
    }
};