class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'

        while len(word) < k:
            new = [chr(ord(char) + 1) for char in word]
            word += ''.join(new)

        return word[k-1]
