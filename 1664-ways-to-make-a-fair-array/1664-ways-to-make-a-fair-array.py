class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        total_even = sum(nums[i] for i in range(0, n, 2))
        total_odd = sum(nums[i] for i in range(1, n, 2))

        count = 0
        prefix_even = 0
        prefix_odd = 0

        for i in range(n):
            if i % 2 == 0:
                suffix_even = total_even - prefix_even - nums[i]
                suffix_odd = total_odd - prefix_odd
            else:
                suffix_even = total_even - prefix_even
                suffix_odd = total_odd - prefix_odd - nums[i]
            
            new_even = prefix_even + suffix_odd
            new_odd = prefix_odd + suffix_even

            if new_even == new_odd:
                count += 1
            
            if i % 2 == 0:
                prefix_even += nums[i]
            else:
                prefix_odd += nums[i]
        return count