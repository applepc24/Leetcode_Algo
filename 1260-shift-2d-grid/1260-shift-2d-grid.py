class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total_element = m * n

        k = k % total_element

        if k == 0:
            return grid
        
        flat_list = []

        for row in grid:
            for val in row:
                flat_list.append(val)
        
        shifted_list = flat_list[-k:] + flat_list[:-k]

        result = []
        for i in range(m):
            row = shifted_list[i * n: (i+1) * n]
            result.append(row)
        return result
        