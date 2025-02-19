class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ['a', 'b', 'c']
        res = []

        def genNext(s: str) -> list[str]:
            res = []
            for l in letters:
                if s[-1] != l:
                    res.append(s + l)
            return res

        curr = ['a','b','c']
        while len(curr[0]) < n+1:
            if len(curr[0]) == n:
                res.extend(curr)
            candidates=[]
            for i in curr:
                candidates.extend(genNext(i))
            curr = candidates
        
        print(res)
        return res[k-1] if k <= len(res) else ""
            
                    
