from typing import List


class Solution:
    def __init__(self):
        self.max_len = 1
        self.start = 0
        self.compare_and = 0

    def longestNiceSubarray(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while self.compare_and & nums[i] != 0:
                self.compare_and &= ~nums[self.start]
                self.start += 1
            self.compare_and |= nums[i]
            self.max_len = max(self.max_len, i - self.start + 1)

        return self.max_len
