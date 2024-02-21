class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        return haystack.find(needle)
    

print(Solution().strStr("sadbutsad", "sad"))
print(Solution().strStr("leetcode", "leeto"))
