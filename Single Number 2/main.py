from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = {}
        for num in nums:
            if not num in result.keys():
                result[num] = 1
            else:
                result[num] += 1
        
        for key, value in result.items():
            if value == 1:
                return key
        
        return 0
    

print(Solution().singleNumber([2,2,1]))
print(Solution().singleNumber([4,1,2,1,2]))
print(Solution().singleNumber([1]))

