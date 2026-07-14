import math
from functools import cache

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        @cache
        def dp(i, g1, g2):
            if i == n:
                return 1 if g1 == g2 and g1 > 0 else 0
            
            ans = 0

            ans += dp(i+1, g1, g2)

            ans += dp(i+1, math.gcd(g1, nums[i]), g2)

            ans += dp(i+1, g1, math.gcd(g2, nums[i]))

            return ans % MOD
        
        return dp(0, 0, 0)

        