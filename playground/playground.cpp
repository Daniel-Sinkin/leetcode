#include <print>
#include <utility>
#include <vector>

using std::print, std::println;

using Vector = std::vector<int>;

auto main() -> int {
    size_t k = 1;
    Vector arr = {1, 2, 3, 4, 5, 6, 7};

    k %= arr.size();
    for (size_t i = 0; i < arr.size(); ++i) {
        std::swap(arr[i], arr[(arr.size() + i - k) % arr.size()]);
        println("{}", arr);
    }
    return EXIT_SUCCESS;
}