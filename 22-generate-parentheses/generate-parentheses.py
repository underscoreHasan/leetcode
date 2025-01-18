class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def isValid(s: str):
            openBr = 0
            for c in s:
                openBr += 1 if c == "(" else -1
            return openBr

        def dfs(s: str):
            if len(s) == 2*n:
                if isValid(s) == 0:
                    res.append(s)
                return
            
            if isValid(s) < 0:
                return
            else:
                dfs(s + "(")
                dfs(s + ")")

        dfs("")

        return res