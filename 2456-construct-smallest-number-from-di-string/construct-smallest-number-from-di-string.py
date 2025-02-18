class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        res = []
        i = 0
        n = len(pattern)
        
        # Loop from 0 to n (inclusive) because we need to process n+1 numbers
        while i < n + 1:
            stack.append(str(i + 1))
            
            # When we hit an "I" or we've processed all characters in the pattern,
            # pop all elements from the stack and append them to the result.
            if i == n or pattern[i] == "I":
                while stack:
                    res.append(stack.pop())
                    
            i += 1
        
        return "".join(res)
