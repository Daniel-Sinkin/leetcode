class Solution {
public:
    int fib(int n) {
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }

        int fib0 = 1;
        int fib1 = 1;
        int fib2 = 0;

        for (int i = 2; i < n; ++i) {
            fib2 = fib1;
            fib1 = fib0;
            fib0 = fib1 + fib2;
        }

        return fib0;
    }
};