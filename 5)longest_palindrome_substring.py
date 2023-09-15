class Solution(object):
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        result = ""
        max_len = 0

        for i in range(len(s)):
            # For odd-length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    max_len = r - l + 1
                    result = s[l:r + 1]
                l = l - 1
                r = r + 1
            
            # For even-length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    max_len = r - l + 1
                    result = s[l:r + 1]
                l = l - 1
                r = r + 1

        return result

s = "babad"
res = Solution().longestPalindrome(s)
print(res)
