class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {} # frequency map

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > 1:
                return True
        return False