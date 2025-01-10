class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: b - a,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(b / a)
        }
        stack = []

        for i in tokens:
            if i not in operations:
                stack.append(int(i))
            else:
                res = operations[i](stack.pop(), stack.pop())
                stack.append(res)
        
        return stack.pop()