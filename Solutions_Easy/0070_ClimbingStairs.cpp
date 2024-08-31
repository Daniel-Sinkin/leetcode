class Solution {
private:
    int memoized[45];

    int _climb_stairs(int n) {
        if (n <= 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        if (memoized[n - 1] == -1) {
            memoized[n - 1] = _climb_stairs(n - 1) + _climb_stairs(n - 2);
        }
        return memoized[n - 1];
    }

public:
    int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 2;
        }
        if (n == 3) {
            return 3;
        }

        memoized[0] = 1;
        memoized[1] = 2;
        for (int i = 2; i < 45; ++i) {
            memoized[i] = -1;
        }

        return _climb_stairs(n);
    }
};