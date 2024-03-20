class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        _prefix = ""
        if len(strs) == 0:
            return _prefix
        if len(strs[0]) == 0:
            return _prefix

        _prefix_candidate = strs[0][0]
        while True:
            for _s in strs:
                if len(_s) == 0:
                    return _prefix
                if _prefix_candidate != _s[0]:
                    return _prefix
            
            _prefix += _prefix_candidate
            for i in range(len(strs)):
                strs[i] = strs[i][1:]
                if len(strs[i]) == 0:
                    return _prefix
                
            _prefix_candidate = strs[0][0]