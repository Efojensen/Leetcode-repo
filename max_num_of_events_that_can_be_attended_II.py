class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key = lambda event: event[0])

        n = len(events)

        next_indices = []
        starts = [e[0] for e in events]

        for i in range(n):
            next_indices.append(bisect_left(starts, events[i][1] + 1))
        
        @lru_cache(None)
        def dp(current_index, count):
            if count == 0 or current_index == n:
                return 0
            
            res = max(events[current_index][2] + dp(next_indices[current_index], count - 1), dp(current_index + 1, count))
            return res
        
        return dp(0, k)
