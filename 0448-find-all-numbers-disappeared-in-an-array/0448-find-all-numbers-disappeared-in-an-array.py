class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        perfect = set(range(1, len(nums) + 1))
        current = set(nums)
        missing = perfect - current
        return list(missing)