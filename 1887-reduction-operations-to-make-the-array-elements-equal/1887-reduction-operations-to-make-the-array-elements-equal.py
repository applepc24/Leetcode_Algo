class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

        nums.sort()
        ops = 0
        total = 0

        n = len(nums)
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                ops += 1
            total += ops
        return total