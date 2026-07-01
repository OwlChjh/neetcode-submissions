class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[-1]:
                if target > nums[-1] and nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            elif nums[mid] <= nums[-1]:
                if target > nums[-1] or nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1

        return left if nums[left] == target else - 1

            


