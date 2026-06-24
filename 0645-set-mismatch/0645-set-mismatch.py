class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expect_sum = n * (n+1) // 2

        actual_sum = sum(nums)

        unique_sum = sum(set(nums))

        dupulicate_num = actual_sum - unique_sum

        missing = expect_sum - unique_sum

        return [dupulicate_num, missing] 

