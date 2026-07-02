import heapq

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1
        
        total_sum = sum(target)
        max_heap = [-x for x in target]
        heapq.heapify(max_heap)

        while True:
            max_val = -heapq.heappop(max_heap)

            if max_val == 1:
                return True
            
            rest_sum = total_sum - max_val

            if rest_sum == 1:
                return True
            
            if rest_sum == 0 or max_val <= rest_sum or max_val % rest_sum == 0:
                return False
            
            prev_val = max_val % rest_sum

            heapq.heappush(max_heap, -prev_val)
            total_sum = total_sum - max_val + prev_val
            
