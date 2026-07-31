from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = list(Counter(word).values())
        freq.sort(reverse=True)

        total = 0
        for i, count in enumerate(freq):
            cost = (i // 8) + 1
            total += count * cost
        
        return total