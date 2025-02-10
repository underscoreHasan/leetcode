class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count = Counter(s1)
        w = len(s1)
        l = 0
        r = w - 1
        candidate = Counter(s2[l:r])

        while r < len(s2):       
            print(candidate)
            candidate[s2[r]] = candidate.get(s2[r], 0) +1
            if candidate == s1count:
                return True
            candidate[s2[l]] -= 1
            candidate += Counter()
            r+=1
            l+=1

        return False