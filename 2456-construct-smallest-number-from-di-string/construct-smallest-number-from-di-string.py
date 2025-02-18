class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        res = []
        
        for i in range(len(pattern) + 1):
            stack.append(str(i + 1))  # Push the next number onto the stack

            if i == len(pattern) or pattern[i] == "I":
                while stack:
                    res.append(stack.pop())  # Pop everything when we see "I" or reach the end
        
        return "".join(res)