class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res: list[str] = []

        start, stop = 0, k

        while True:
            if stop >= len(s):
                test = s[start:]
                length = len(test)
                if length == k:
                    res.append(test)
                else:
                    diff = k - length
                    test += (fill * diff)
                    res.append(test)
                break
            test = s[start: stop]
            res.append(test)
            start += k
            stop += k

        return res
