class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()
        sign = 1
        result = 0
        if s and (s[0] == '-' or s[0] == '+'):
            if s[0] == '-':
                sign = -1
            s = s[1:]
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break
        result *= sign
        if result > 2**31 - 1:
            return 2**31 - 1
        elif result < -2**31:
            return -2**31
        return result

s = "42"
result = Solution().myAtoi(s)
print(result)
