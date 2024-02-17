class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        s = s.lower()
        for c in s:
            if c.isalnum():
                result += c
        
        return result == result[::-1]

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome(" "))

