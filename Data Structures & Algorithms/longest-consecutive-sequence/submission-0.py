class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for num in s:
            # start the streak
            if num - 1 not in s:
                streak = 1
                while num + 1 in s:
                    streak += 1
                    num += 1
                ans = max(ans, streak)
        return ans