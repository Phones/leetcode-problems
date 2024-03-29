from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = {}
        for num in nums:
            result ^= num

        return result


print(Solution().singleNumber([2, 2, 1]))
print(Solution().singleNumber([4, 1, 2, 1, 2]))
print(Solution().singleNumber([1]))
