#include <bitset>
#include <iostream>
#include <print>
#include <string>
#include <utility>
#include <vector>

using std::print, std::println;

auto main() -> int {
    using std::vector;
    vector<vector<char>> board = {
        {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
        {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
        {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
        {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
        {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
        {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'}};

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

    for (const vector<char> &row : board) {
        std::bitset<9> row_pattern{0b0000'0000};
        for (char entry : row) {
            if (entry != '.') {
                int idx = entry - '1';
                if (row_pattern.test(idx)) return false;
                row_pattern.set(idx);
            }
        }
    }
    for (size_t col_idx = 0; col_idx < 9; ++col_idx) {
        std::bitset<9> col_pattern1{0b0000'0000};
        std::bitset<9> col_pattern2{0b0000'0000};
        std::bitset<9> col_pattern3{0b0000'0000};
        std::bitset<9> col_pattern4{0b0000'0000};
        for (size_t i = 0; i < 9; ++i) {
            vector<char> board[i];

            char c1 = board[i] board[col_idx]
        }
    }
}