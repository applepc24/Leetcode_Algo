class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT, MAX_INT = -2**31, 2**31 - 1

        reversed_str = str(abs(x))[::-1]

        reversed_num = int(reversed_str)

        if x < 0:
            reversed_num *= -1
        
        if reversed_num < MIN_INT or reversed_num > MAX_INT:
            return 0
        return reversed_num
        