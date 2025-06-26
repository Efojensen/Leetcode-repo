class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ans, length = 0, len(s) -1
        val = 0
        for i in range(length, -1, -1):
            if s[i] == "0":
                ans += 1
            else:
                pos = length - i
                if val + (1 << pos) <= k:
                    val += (1 << pos)
                    ans += 1
        
        return ans
