class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)

        total = 0
        for i in range(n):
            cost = (i // 8) + 1
            total += cost
        
        return total