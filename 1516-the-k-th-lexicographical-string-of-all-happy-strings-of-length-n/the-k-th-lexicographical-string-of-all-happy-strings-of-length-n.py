class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        letters = ['a','b','c']

        def genNext(s: str) -> list[str]:
            res = []
            for l in letters:
                if s[-1] != l:
                    res.append(s + l)
            return res

        curr = ['a','b','c']
        while len(curr[0]) <= n:
            if len(curr[0]) == n:
                res.extend(curr)
                break
            candidates=[]
            for i in curr:
                candidates.extend(genNext(i))
            curr = candidates
        
        return res[k-1] if k <= len(res) else ""
            
                    
