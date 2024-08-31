class Solution:
    def productString(self, s1: list[str], s2: str) -> list[str]:
        lst = []
        for s11 in s1:
            for s22 in s2:
                lst.append(s11 + s22)
        return lst

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        digit_to_letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        strings = [c for c in digit_to_letter[digits[0]]]
        for digit in digits[1:]:
            strings = self.productString(strings, digit_to_letter[digit])
        return strings
