class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        ans = 0
        length = 1
        i = 0

        while length < k:
            if operations[i] == 1:
                ans += 1

            length *= 2
            i += 1

        while i > 0:
            i -= 1
            half = length // 2
            if k > half:
                k -= half
            else:
                if operations[i] == 1:
                    ans -= 1
            length = half

        return chr(ord('a') + (ans % 26))
