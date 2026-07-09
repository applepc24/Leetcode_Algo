class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainer_map = {0: -1}
        current_sum = 0

        for i, num in enumerate(nums):
            current_sum += num

            remainer = current_sum % k

            if remainer in remainer_map:
                if i - remainer_map[remainer] >= 2:
                    return True
            else:
                remainer_map[remainer] = i
        return False