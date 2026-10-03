class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = list()
        max_area = 0

        for index,height in enumerate(heights):
            start = index
            while stack and stack[-1][0] > height:
                top_height, top_index = stack.pop()

                max_area = max(max_area,top_height*(index-top_index))
                start = top_index
            stack.append((height,start))

        for h, start in stack:
            max_area = max(max_area, h*(len(heights) - start))
        
        return max_area

        