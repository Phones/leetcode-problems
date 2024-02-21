from typing import List


class Solution:
    def __init__(self) -> None:
        self.first_exec = True

    def search(self, nums: List[int], target: int, start: int = 0, end: int = 0) -> int:
        if self.first_exec:
            self.first_exec = False
            start, end = 0, len(nums) - 1

        if start == end:
            if nums[start] == target:
                return start

            return -1

        meio = (start + end) // 2
        if nums[meio] < target:
            return self.search(nums, target, meio + 1, end)

        return self.search(nums, target, start, meio)


print(Solution().search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8))
