class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        
        longest_subset = 1
        for i, _s1 in enumerate(s):
            charset = {_s1}
            for j, _s2 in enumerate(s[i+1:]):
                if _s2 not in charset:
                    charset.add(_s2)
                else:
                    i = j
                    break
            longest_subset = max(longest_subset, len(charset))

        return longest_subset