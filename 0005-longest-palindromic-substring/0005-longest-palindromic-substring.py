class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s
        
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right +=1

            return s[left + 1:right]
        
        longest = ""

        for i in range(len(s)):
            odd_pal = expand_around_center(i, i)

            even_pal = expand_around_center(i, i + 1)

            longest = max(longest, odd_pal, even_pal, key = len)

        return longest