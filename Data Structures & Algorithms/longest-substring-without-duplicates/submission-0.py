class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs = set()
        l = 0
        ans = 0

        for r, x in enumerate(s):
            while subs and s[r] in subs:
                subs.remove(s[l])
                l += 1
            subs.add(x)
            ans = max(ans, r - l + 1)

        return ans
