class Solution:
     def possibleStringCount(self, word: str) -> int:
        if not word:
            return 0
        
        n = len(word)
        
        count = 1
        
        i = 0
        while i < n:
            j = i

            while j < n and word[j] == word[i]:
                j += 1
            
            run_length = j - i
            if run_length >= 2:
                # We can remove 1 to (run_length - 1) duplicates
                count += (run_length - 1)
            
            i = j
        
        return count
