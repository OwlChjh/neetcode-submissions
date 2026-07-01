class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # O(n)
        heights.append(-1)  # Add sentinel to flush stack
        st = [-1]
        max_area = 0

        for i, h in enumerate(heights):
            # maintain an increasing stack
            while len(st) > 1 and h <= heights[st[-1]]: 
                height = heights[st.pop()]
                width = i - st[-1] - 1
                max_area = max(max_area, height * width)
            st.append(i)

        return max_area