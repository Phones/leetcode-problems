from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = [0 for i in range(len(nums) + 1)]
        for num in nums:
            result[num] += 1

        for index, num in enumerate(result):
            if num == 0:
                return index

        return -1

class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return nums [0] - 1
        len_ = len(nums)
        for i in range(len_):
            if i + 1 == len_ or nums[i + 1] - nums[i] > 1:
                return i + 1
            
        return -1

class Solution3:
    def missingNumber(self, nums: List[int]) -> int:        
        return sum(range(0, len(nums) + 1)) - sum(nums)

class Solution4:
    # Solução usando a formula de gauss para soma
    def missingNumber(self, nums: List[int]) -> int:        
        n = len(nums)
        return ((n * (n + 1)) // 2) - sum(nums)

print(Solution4().missingNumber([0,1]))
