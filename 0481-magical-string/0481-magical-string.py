class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            return 1
        
        s = [1, 2, 2]
        idx = 2

        while len(s) < n:
            next_char = 3 - s[-1]
            group_len = s[idx]

            s.extend([next_char] * group_len)
            idx += 1
        return s[:n].count(1)