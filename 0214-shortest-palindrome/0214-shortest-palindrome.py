class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        combined = s + "#" + s[::-1]
        n = len(combined)
        failure = [0] * n
        
        for i in range(1, n):
            j = failure[i-1]
            while j > 0 and combined[i] != combined[j]:
                j = failure[j-1]
            if combined[i] == combined[j]:
                j += 1
            failure[i] = j
        
        longest_palindrome_len = failure[-1]
        remaining = s[longest_palindrome_len:]
        
        return remaining[::-1] + s
