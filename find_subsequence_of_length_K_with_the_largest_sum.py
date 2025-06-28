class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for value in nums:
            ans.append(value)
            if len(ans) > k:
                least = min(ans)
                ans.remove(least)

        return ans
