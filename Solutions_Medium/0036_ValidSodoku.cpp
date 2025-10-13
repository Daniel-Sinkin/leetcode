class Solution {
public:
    bool isValidSudoku(vector<vector<char>> &board) {
        std::array<std::bitset<9>, 9> row_bits{};
        std::array<std::bitset<9>, 9> col_bits{};
        std::array<std::bitset<9>, 9> block_bits{};

        for (size_t row = 0; row < 9; ++row) {
            for (size_t col = 0; col < 9; ++col) {
                char c = board[row][col];
                if (c == '.') continue;

                int bit = c - '1';
                size_t block = (row / 3) * 3 + (col / 3);

                if (row_bits[row].test(bit) ||
                    col_bits[col].test(bit) ||
                    block_bits[block].test(bit)) {
                    return false;
                }

                row_bits[row].set(bit);
                col_bits[col].set(bit);
                block_bits[block].set(bit);
            }
        }
        return true;
    }
};