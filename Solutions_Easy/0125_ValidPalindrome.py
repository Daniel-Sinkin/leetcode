import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Uppercase -> Lowercase
        s = s.lower()
        # Removes all non-alphanumeric chars
        s = re.sub(r"[^a-z0-9]", "", s)

        for s1, s2 in zip(s[: len(s) // 2], s[::-1]):
            if s1 != s2:
                return False
        return True
