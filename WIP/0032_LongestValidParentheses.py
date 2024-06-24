def longestValidParentheses(s: str) -> int:
    diff = 1
    count = 0
    while diff != 0:
        s_new = s.replace("()", "")
        diff = len(s) - len(s_new)
        count += diff
        s = s_new
    return count


"""
s =
"()(()"
Output: 4
Expected: 2

The pattern should be something like this:
max(f("(()"), f("()(")) + 1
"""
