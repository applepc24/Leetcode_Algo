class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        failure = [0] * n

        for i in range(1, n):
            j = failure[i-1]
            while j > 0 and s[i] != s[j]:
                j = failure[j-1]
            if s[i] == s[j]:
                j += 1
            failure[i] = j
        return s[:failure[-1]]