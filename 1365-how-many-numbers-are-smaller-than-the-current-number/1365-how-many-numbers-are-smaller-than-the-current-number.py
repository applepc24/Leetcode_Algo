class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_num = sorted(nums)

        num_of_count = {}
        for i, num in enumerate(sorted_num):
            if num not in num_of_count:
                num_of_count[num] = i

        ans = []
        for num in nums:
            count = num_of_count[num]
            ans.append(count)
        return ans

        