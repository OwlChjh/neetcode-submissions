class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)

        if n > m:
            return False

        target = Counter(s1)
        window = Counter(s2[:n])

        if window == target:
            return True
        
        for i in range(n, m):
            window[s2[i]] += 1

            left_ch = s2[i - n]
            window[left_ch] -= 1

            if window[left_ch] == 0:
                del window[left_ch]
            
            if window == target:
                return True
        return False