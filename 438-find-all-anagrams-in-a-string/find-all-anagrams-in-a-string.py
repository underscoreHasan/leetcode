class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pCount = Counter(p)
        windowCount = Counter()
        l = 0
        res = []

        for r in range(len(s)):
            windowCount.update(s[r])

            while r - l + 1 > len(p):
                windowCount.subtract(s[l])
                if windowCount[s[l]] == 0:
                    del windowCount[s[l]]
                l += 1
            
            if windowCount == pCount:
                res.append(l)

        return res
        
            
