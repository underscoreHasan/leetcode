class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        freq = Counter(map(str, digits))
        for n in range(100, 1000, 2):
            if Counter(str(n)) <= freq:
                res.append(n)
            
        return res