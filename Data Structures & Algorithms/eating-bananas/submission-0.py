class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k: bananas/hour 
        m = max(piles)

        # apply binary search on range (1, m)

        left, right = 1, m
        while left < right:
            mid = left + (right - left) // 2
            if sum(math.ceil(pile / mid) for pile in piles) <= h:
                right = mid
            else:
                left = mid + 1
        return left
