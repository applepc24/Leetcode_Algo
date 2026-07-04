class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital_count = 0

        for char in word:
            if 'A' <= char <= 'Z':
                capital_count += 1
            
        if capital_count == len(word):
            return True
            
        if capital_count == 0:
            return True
            
        if capital_count == 1 and 'A' <= word[0] <= 'Z':
            return True
        return False