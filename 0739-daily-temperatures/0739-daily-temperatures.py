class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i, tmp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < tmp:
                waiting_idx = stack.pop()
                ans[waiting_idx] = i - waiting_idx
            
            stack.append(i)
        return ans