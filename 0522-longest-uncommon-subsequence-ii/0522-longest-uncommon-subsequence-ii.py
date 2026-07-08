class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        
        def is_sub(word1: str, word2: str) -> bool:
            i, j = 0, 0
            
            while i < len(word1) and j < len(word2):
                if word1[i] == word2[j]:
                    i += 1
                j += 1
            return i == len(word1)
        
        strs.sort(key = len, reverse=True)

        for i, target_word in enumerate(strs):
            is_valid = True

            for j, other_word in enumerate(strs):
                if i == j:
                    continue

                if is_sub(target_word, other_word):
                    is_valid = False
                    break
            
            if is_valid:
                return len(target_word)
        return -1
