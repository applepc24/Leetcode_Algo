class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        memo = {1: [1]}

        def helper(n):
            if n in memo:
                return memo[n]
            
            left_size = (n+1) // 2
            right_size = n // 2

            left = helper(left_size)
            right = helper(right_size)

            result = [2*x-1 for x in left] + [2*x for x in right]

            memo[n] = result
            return result
        return helper(n)
