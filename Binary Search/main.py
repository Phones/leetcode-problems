from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while True:
            if start == end:
                if nums[start] == target:
                    return start
                return -1

            meio = (start + end) // 2
            if nums[meio] < target:
                start = meio + 1
            else:
                end = meio


print(Solution().search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8))
