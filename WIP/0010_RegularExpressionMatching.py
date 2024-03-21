class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        dp = []
        for i in range(len(s) + 1):
            dp.append([])
            for j in range(len(p) + 1):
                dp[-1].append(False)

        # "", "" matches
        dp[0][0] = True
        
        for i in range(1, len(s) + 1):
            dp[i][0] = False # s, "" can't match if s != ""

        for j in range(1, len(p) + 1):
            # Can only match "" with pattern X iff X consists only of *
            dp[0][j] = dp[0][j - 1] and (p[j - 1] == "*")

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == ".":
                    dp[i][j] = dp[i - 1][j - 1] # Match any char and check if what came before matches
                elif p[j - 1] == "*":
                    # Either make * into . to match last char of current s string slice or into ""
                    dp[i][j] = dp[i][j - 1] or self.isMatch(s[i:], "*" + p[j:])
                else:
                    # Same as with . just that also have to check against current char
                    dp[i][j] = (s[i - 1] == p[j - 1]) and dp[i - 1][j - 1]
            self.print_matrix(dp)
            print()

        return dp[-1][-1]

    def print_matrix(self, M: list[list[any]]) -> None:
        for row in M:
            _s = "["
            for j, c in enumerate(row):
                _s += ("1" if c else "0")
                if j != len(row) - 1:
                    _s += ", "
            _s += "]"
            print(_s)