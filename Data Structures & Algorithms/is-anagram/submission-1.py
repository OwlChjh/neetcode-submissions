class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {} # frequency map
        for i in s:
            freq[i] = freq.get(i, 0) + 1

        for j in t:
            if j not in freq:
                return False
            freq[j] -= 1
        
        for value in freq.values():
            if value != 0:
                return False
        
        return True