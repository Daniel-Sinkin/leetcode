""" Initial attempt
# Brute force is way too slow on the * case
# (isMatch "" y) <=> (y = "" or y = *^n)
if len(s) == 0:
    # Empty string can only match with empty or all wildcard pattern
    return all(_p == "*" for _p in p)

# (isMatch s "") <=> (s = "")  ## Empty pattern
if len(p) == 0:
    return s == ""
elif len(p) == 1: # isMatch s 'a'
    if p == "*": # * matches with everything
        return True
    elif p == "?": # ? matches with exactly one char
        return (len(s) == 1)
    else: # chars have to agree
        return p == s
else:
    if p[0] == "?":
        # "?X", "aY" -> ? = a and we have to match "X", "Y"
        return self.isMatch(s[1:], p[1:])
    elif p[0] == "*":
        # ** == *, so we can gobble up all the * and consolidate them to one
        p = p.lstrip("*")
        if p == "": # p = *^n
            return True
        # This is the tricky case
        # have to check * taking "", one char, two chars, ...
        return any(self.isMatch(s[i:], p) for i in range(len(s)))
    else:
        return (s[0] == p[0]) and self.isMatch(s[1:], p[1:])
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # using dynamic programming approach to improve on the previous bruteforce
        # s = "adceb"
        # p = "*a*b"

        # First column: "", "" matches and "X", "" never matches for len(X) > 0
        # First row, "", "" matches, "", Xb matches iff a == * and "", X matches
        # [1, 1, 0, 0, 0]
        # [0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0] 

        # Final dp matrix, note that if we have a * that matches somewhere, the remainder
        # of the column matches, might be potential speedup
        # Could also maybe traverse from bottom right corner somehow to avoid
        # having to check every entry in the matrix.
        # [1, 1, 0, 0, 0]
        # [0, 1, 1, 1, 0]
        # [0, 1, 0, 1, 0]
        # [0, 1, 0, 1, 0]
        # [0, 1, 0, 1, 0]
        # [0, 1, 0, 1, 1]

        dp = []
        for i in range(len(s) + 1):
            dp.append([])
            for j in range(len(p) + 1):
                dp[-1].append(False)

        dp[0][0] = True
        
        for i in range(1, len(s) + 1):
            dp[i][0] = 0 # s, "" can't match if s != ""

        for j in range(1, len(p) + 1):
            dp[0][j] = dp[0][j - 1] and (p[j - 1] == "*")

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1] # Match any char and check if what came before matches
                elif p[j - 1] == "*":
                    # Either make * into ? to match last char of current s string slice or into ""
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                else:
                    # Same as with ? just that also have to check against current char
                    dp[i][j] = (s[i - 1] == p[j - 1]) and dp[i - 1][j - 1]

        return dp[-1][-1]


def isMatch(s: str, p: str) -> bool:
    p = "*?d?"
    s = "abcde"

    dp = [[False] * len(p)] * len(s)

    # i = 0
    for j in range(len(p)):
        dp[0][j] = (p[j] == "*") # Only * matches empty string

    # s, [*, x:Y] matches iff s, [x:Y] or s[1:], [*x:Y] matches
    # Case p[i + 1] == "?" implies dp[i+1][j] == dp[i][j-1] b.c.
    # Ya, X? matches if ? = a and Y, X matches
    # Case p[i + 1] == * implies 
    # Case p[i + 1] is __CHAR__ requires s[i + 1
    raise NotImplementedError("WIP")

def print_matrix(M: list[list[any]]) -> None:
    for row in M:
        _s = "["
        for j, c in enumerate(row):
            _s += ("1" if c else "0")
            if j != len(row) - 1:
                _s += ", "
        _s += "]"
        print(_s)
    print(str("\n".join("[" + (", ".join(x)) + "]") for y in M for x in y))

if __name__ == "__main__":
    p = "*a*b"
    s = "adceb"

    