class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def isValid(s: str):
            openBr = 0
            for c in s:
                openBr += 1 if c == "(" else -1
                if openBr < 0:
                    return False
            return not openBr

        def dfs(s: str):
            if len(s) == 2*n:
                if isValid(s):
                    res.append(s)
                return

            dfs(s + "(")
            dfs(s + ")")

        dfs("")

        return res