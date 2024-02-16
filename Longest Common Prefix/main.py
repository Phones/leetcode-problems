from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        fisrt_str = strs[0]
        for index, c in enumerate(fisrt_str):
            for str_ in strs:
                if index >= len(str_) or not str_[index] == c:
                    return result
            
            result += c

        return result

print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))
print(Solution().longestCommonPrefix(["a"]))

