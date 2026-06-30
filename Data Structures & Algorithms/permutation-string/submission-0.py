class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        cnt1 = defaultdict(int)
        for ch in s1:
            cnt1[ch] += 1
        cnt2 = defaultdict(int) # frequency map for substring with length n of s2
        left = 0
        for right, ch in enumerate(s2):
            cnt2[ch] += 1
            if (right - left + 1) > n:
                cnt2[s2[left]] -= 1
                if cnt2[s2[left]] == 0:
                    del cnt2[s2[left]]
                left += 1

            if (right - left + 1) == n:
                if cnt1 == cnt2:
                    return True

        return False