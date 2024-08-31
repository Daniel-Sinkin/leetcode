class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_list = [0] * 26
        t_list = [0] * 26
        for sc, tc in zip(s, t):
            s_list[ord(sc) - 97] += 1
            t_list[ord(tc) - 97] += 1

        for so, to in zip(s_list, t_list):
            if so != to:
                return False

        return True
