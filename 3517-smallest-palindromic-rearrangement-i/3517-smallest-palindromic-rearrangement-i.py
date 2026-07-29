from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)

        half = []
        middle = ""

        for ch in sorted(count.keys()):
            c = count[ch]
            half.append(ch * (c // 2))
            if c % 2 == 1:
                middle = ch
            
        left = "".join(half)
        right = left[::-1]

        return left + middle + right
        