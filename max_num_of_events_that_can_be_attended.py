import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])  # Sort by start day
        max_day = max(end for _, end in events)
        heap = []
        count = 0
        i = 0  # Pointer for events list
        n = len(events)
        
        for d in range(1, max_day + 1):
            # Add all events that start on day 'd' to the heap
            while i < n and events[i][0] == d:
                heapq.heappush(heap, events[i][1])  # Push end day
                i += 1
            
            # Remove events that are already over before 'd'
            while heap and heap[0] < d:
                heapq.heappop(heap)
            
            # Attend the earliest ending event
            if heap:
                heapq.heappop(heap)
                count += 1
        
        return count
