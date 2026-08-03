class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        n = len(arr)
        min_diff = min(arr[i+1] - arr[i] for i in range(n-1))

        result = []

        for i in range(n-1):
            if arr[i+1] - arr[i] == min_diff:
                result.append([arr[i], arr[i+1]])
        return result