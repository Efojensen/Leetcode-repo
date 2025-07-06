from collections import defaultdict

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq1 = defaultdict(int)
        for num in nums1:
            self.freq1[num] += 1
        self.freq2 = defaultdict(int)
        for num in nums2:
            self.freq2[num] += 1

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        self.freq2[old_val] -= 1
        new_val = old_val + val
        self.nums2[index] = new_val
        self.freq2[new_val] += 1

    def count(self, tot: int) -> int:
        res = 0
        for num in self.freq1:
            complement = tot - num
            res += self.freq1[num] * self.freq2.get(complement, 0)
        return res
