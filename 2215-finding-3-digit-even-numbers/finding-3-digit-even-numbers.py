class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # import itertools

        #res = []
        # def checkConditions(n: int):
        #     if int(str(n)[0]) != 0 and n%2 ==0 and len(str(n)) == 3:
        #         return True
        
        # perms = list(itertools.permutations(digits, 3))
        # for n in perms:
        #     if checkConditions(int(''.join(str(x) for x in n))):
        #         res.append(int(''.join(str(x) for x in n)))
        
        # return sorted(res)

        res = []
        freq = Counter(map(str, digits))
        for n in range(100, 1000, 2):
            if Counter(str(n)) <= freq:
                res.append(n)
            
        return res