class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        bracket_map  = {")":"(","}":"{","]":"["}

        for char in s: 

            if char not in bracket_map:
                stack.append(char)

            else:
                top_element = stack.pop() if stack else '#'

                if bracket_map[char] != top_element:
                    return False
        return len(stack) == 0
        