class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_to_right = [nums[0]] * n
        right_to_left = [nums[-1]] * n
        for i in range(len(nums[1:])):
            left_to_right[i + 1] = left_to_right[i] * nums[i + 1]
            right_to_left[n - i - 2] = right_to_left[n - i - 1] * nums[n - i - 2]

        retval = [right_to_left[1]] + ([1] * (n - 2)) + [left_to_right[-2]]

        for i, x in enumerate(nums[1:-1]):
            retval[i + 1] = left_to_right[i] * right_to_left[i + 2]
        return retval
