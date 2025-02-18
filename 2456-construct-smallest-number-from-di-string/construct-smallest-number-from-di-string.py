class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        res = []
        n = len(pattern)
        i = 0

        while i < n + 1:
            # Always push the next number onto the stack.
            stack.append(str(i + 1))

            # If we're at the end of the pattern, flush the stack.
            if i == n:
                while stack:
                    res.append(stack.pop())
            else:
                # Explicit condition when an "I" is encountered.
                if pattern[i] == "I":
                    while stack:
                        res.append(stack.pop())
                # Explicit condition when a "D" is encountered.
                elif pattern[i] == "D":
                    # When a "D" is encountered, we do not flush the stack.
                    # The stack will be flushed later when an "I" is encountered
                    # or at the end of the loop.
                    pass

            i += 1

        return "".join(res)
