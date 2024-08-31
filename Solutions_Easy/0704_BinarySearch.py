class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ptr_left = 0
        ptr_right = n - 1

        while ptr_right - ptr_left > 1:
            mid = (ptr_right + ptr_left) // 2
            print(f"{ptr_left=},{ptr_right=},{mid=}")
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                ptr_left = mid
            else:
                ptr_right = mid

        if nums[ptr_right] == target:
            return ptr_right
        if nums[ptr_left] == target:
            return ptr_left
        return -1
