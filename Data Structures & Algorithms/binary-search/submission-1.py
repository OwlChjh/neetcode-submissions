class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)

        while l < r: # range exist: when l == r [l, r) is empty, exit while loop
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid # [left, mid)
            else: 
                l = mid + 1 # [mid+1, right)
        return -1

