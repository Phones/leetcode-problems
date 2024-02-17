class Solution:
    def reverse(self, x: int) -> int:
        str_ = str(x)
        result = 0
        if str_[0] == "-":
            str_ = str_[1:]
            result = int(f"-{str_[::-1]}")
        else:
            result = int(str_[::-1])
        
        if -2147483648 <= result <= 2147483647:
            return result

        return 0

print(Solution().reverse(-123))
print(Solution().reverse(123))
