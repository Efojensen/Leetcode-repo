class Solution:
    def mergeSort(self, arr: list[int]):
        if len(arr) <= 1:
            return
        left = arr[:len(arr) // 2]
        right = arr[len(arr) // 2:]

        self.mergeSort(left)
        self.mergeSort(right)

        i, j = 0, 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            k += 1; i += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1; k += 1

    def findLucky(self, arr: List[int]) -> int:
        self.mergeSort(arr)

        counts = Counter(arr)
        luckyInt = -1

        for number in arr:
            if number == counts[number]:
                luckyInt = max(number, luckyInt)

        return luckyInt
