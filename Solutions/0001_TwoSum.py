class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}
        for i, x in enumerate(nums):
            if x in _dict:
                return [i, _dict[x]]
            else:
                _dict[target - x] =  i