class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)

        if n < m:
            return ""

        l = 0
        length = math.inf
        cnt = Counter(t)
        missing = len(t)

        targetLeft, targetRight = 0, n - 1

        for r, x in enumerate(s):
            if cnt[x] > 0: # x in t
                missing -= 1
            cnt[x] -= 1 # if x not in t only in s, cnt[x] = -1

            while missing == 0:
                if r - l + 1 < length:
                    targetLeft = l
                    targetRight = r
                    length = r - l + 1

                cnt[s[l]] += 1
                if cnt[s[l]] > 0:
                    missing += 1
                l += 1

        return "" if length == math.inf else s[targetLeft : targetRight + 1]