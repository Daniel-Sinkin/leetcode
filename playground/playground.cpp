#include <iostream>
#include <print>
#include <string>
#include <utility>
#include <vector>

using std::print, std::println;

auto main() -> int {
    std::string s = "hellomynameisdaniel";

    for (const char &s_char : s) {
        auto x = s_char - 'a';
    }
}