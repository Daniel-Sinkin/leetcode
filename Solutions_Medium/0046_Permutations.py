class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        else:
            temp = []
            for L in self.permute(nums[1:]):
                for i in range(len(L) + 1):
                    temp.append(L[:i] + [nums[0]] + L[i:])
            return temp
