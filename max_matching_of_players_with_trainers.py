class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        self.sortWithMerge(players)
        self.sortWithMerge(trainers)

        i, j = 0, 0
        count = 0
        players_len, trainers_len = len(players), len(trainers)

        while i < players_len and j < trainers_len:
            if players[i] <= trainers[j]:
                count += 1
                i += 1; j += 1
            else:
                j += 1
        
        return count

    
    def sortWithMerge(self, array: list[int]):
        if len(array) <= 1:
            return
        
        left_arr = array[:len(array) // 2]
        right_arr = array[len(array) // 2:]

        self.sortWithMerge(left_arr)
        self.sortWithMerge(right_arr)

        # index of left and right arrays
        i, j = 0, 0
        # index of sorted arrays
        k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                array[k] = left_arr[i]
                i += 1
            else:
                array[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr):
            array[k] = left_arr[i]
            i += 1; k += 1
        
        while j < len(right_arr):
            array[k] = right_arr[j]
            j += 1; k += 1
