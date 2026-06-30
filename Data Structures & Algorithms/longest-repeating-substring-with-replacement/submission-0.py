class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        cnt = defaultdict(int)
        ans = 0
        max_cnt = 0 # most common ch
        for r, x in enumerate(s):
                cnt[x] += 1
                max_cnt = max(max_cnt, cnt[x]) 
                while max_cnt + k < r - l + 1: # k not big enough, update left pointer
                    cnt[s[l]] -= 1
                    l += 1
                ans = max(ans, r - l + 1)
        return ans





