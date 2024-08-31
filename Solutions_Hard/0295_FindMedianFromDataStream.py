from bisect import bisect_left


class MedianFinder:
    def __init__(self):
        self.nums = None

    def addNum(self, num: int) -> None:
        if self.nums == None:
            self.nums = [num]
        else:
            idx = bisect_left(self.nums, num)
            self.nums = self.nums[:idx] + [num] + self.nums[idx:]

    def findMedian(self) -> float:
        if self.nums is None:
            return 0.0

        if len(self.nums) == 1:
            return self.nums[0]
        elif len(self.nums) == 2:
            return (self.nums[0] + self.nums[1]) / 2.0

        if len(self.nums) % 2 == 1:
            return self.nums[len(self.nums) // 2]
        else:
            return (
                self.nums[len(self.nums) // 2 - 1] + self.nums[len(self.nums) // 2]
            ) / 2.0
