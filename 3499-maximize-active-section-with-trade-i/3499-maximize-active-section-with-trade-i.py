class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = '1' + s + '1'
        n = len(t)
    
        blocks = []  # (char, length)
        i = 0
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            blocks.append((t[i], j - i))
            i = j
    
        count1 = s.count('1')
        best = 0
        for idx in range(1, len(blocks) - 1):  # 양끝 경계 블록 제외
            ch, length = blocks[idx]
            if ch == '1':
                gain = blocks[idx - 1][1] + blocks[idx + 1][1]
                best = max(best, gain)
    
        return count1 + best


        
    


        