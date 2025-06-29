class Solution:
    def merge(self, nums: list[int]):
        if len(nums) <= 1:
            return
        left = nums[:len(nums) // 2]
        right = nums[len(nums)// 2:]

        self.merge(left)
        self.merge(right)

        # left and right indexes
        i, j = 0, 0
        # merge array index
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1; k += 1
        
        while j < len(right):
            nums[k] = right[j]
            j += 1; k += 1
            

    def numSubseq(self, nums: List[int], target: int) -> int:
        self.merge(nums)
        ans = 0
        modulo = 10**9 + 7
        prime, secondth = 0, len(nums) - 1

        powers = [1] * (len(nums) + 1)
        
        for i in range(1, len(nums) + 1):
            powers[i] = (powers[i - 1] * 2) % modulo
        
        while prime <= secondth:
            if nums[prime] + nums[secondth] <= target:
                ans = (ans + powers[secondth - prime]) % modulo
                prime += 1
            else:
                secondth -= 1
            
        return ans

