class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0

        left, right = 0, len(heights) - 1

        while left < right:
            width = right - left
            if heights[left] < heights[right]:
                h = heights[left]
                left += 1
            else:
                h = heights[right]
                right -= 1
            
            ans = max(ans, h * width)

            
        return ans
