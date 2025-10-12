ZERO_COUNTS = []
BASELINE = ord("a")


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            cnt = [0] * 26
            for c in word:
                cnt[ord(c) - BASELINE] += 1
            key = tuple(cnt)
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())
