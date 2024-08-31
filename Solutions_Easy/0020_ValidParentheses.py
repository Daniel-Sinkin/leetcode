class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in close_to_open:
                if len(stack) == 0 or stack.pop() != close_to_open[c]:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
