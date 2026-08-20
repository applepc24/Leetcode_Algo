from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        row_reserved = defaultdict(int)

        for row, seat in reservedSeats:
            row_reserved[row] |= (1 << seat)
        
        block1 = (1<<2) | (1<<3) | (1<<4) | (1<<5)
        block2 = (1<<4) | (1<<5) | (1<<6) | (1<<7)
        block3 = (1<<6) | (1<<7) | (1<<8) | (1<<9) 

        result = 0

        for row, mask in row_reserved.items():
            count = 0

            if not (mask & block1):
                count += 1
                mask |= block1
            if not (mask & block3):
                count += 1
                mask |= block3
            elif not (mask & block2):
                count += 1
            
            result += count
        
        result += (n - len(row_reserved)) * 2
        return result                