class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = {}

        for i in range(n - k + 1):
            window = set(nums[i:i+k])
            for val in window:
                count[val] = count.get(val, 0) + 1
            
        candinates = [val for val, c in count.items() if c == 1]
        if candinates:
            return max(candinates)
        else:
            return -1
