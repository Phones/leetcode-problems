from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_integers = {}
        for index, num in enumerate(nums):
           dict_integers[num] = index
                
        for index, num in enumerate(nums):
            aux = target - num
            if dict_integers.get(aux) is not None:
                if index == dict_integers[aux]:
                    continue

                return [index, dict_integers[aux]]

        return []

result = Solution().twoSum([1,7,3,4,6,3,8,0,9], 10)
print(result)
