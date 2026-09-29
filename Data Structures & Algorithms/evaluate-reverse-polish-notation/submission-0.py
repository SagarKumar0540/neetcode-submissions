import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()

        ops = {
            "+":operator.add,
            "-":operator.sub,
            "*":operator.mul,
            "/":lambda a,b: int(a/b)
        }

        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[token](a,b))
            else:
                stack.append(int(token))
        return stack[-1]
        