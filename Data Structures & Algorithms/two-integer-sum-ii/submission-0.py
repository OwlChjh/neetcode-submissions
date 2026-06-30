class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            while left < right and numbers[left] + numbers[right] < target:
                left += 1
            
            while left < right and numbers[left] + numbers[right] > target:
                right -= 1
            
            if left < right and numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]