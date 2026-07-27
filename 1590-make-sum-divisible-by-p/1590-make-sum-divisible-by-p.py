class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        r = total % p

        if r == 0:
            return 0
        
        n = len(nums)
        best = n

        last_index = {0: -1}

        prefix = 0

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p

            target = (prefix - r + p) % p

            if target in last_index:
                length = i - last_index[target]
                best = min(best, length)
            
            last_index[prefix] = i
        return best if best < n else -1