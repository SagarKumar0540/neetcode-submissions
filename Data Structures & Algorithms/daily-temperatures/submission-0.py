class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = list()

        for i,temp in enumerate(temperatures):

            while stack and stack[-1][0] < temp:
                stack_top,stack_top_index = stack.pop()
                result[stack_top_index] = i-stack_top_index

            stack.append((temp,i))

        return result
        