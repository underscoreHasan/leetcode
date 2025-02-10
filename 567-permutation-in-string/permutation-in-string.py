class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1) - 1
        s1count = [0]*26
        candidate = [0]*26

        if len(s1)>len(s2):
            return False
        
        for i in range(len(s1)):
            s1count[ord(s1[i])-ord('a')] += 1
            candidate[ord(s2[i])-ord('a')] += 1

        print(s1count)

        while r < len(s2):
            if s1count == candidate:
                return True
            candidate[ord(s2[l])-ord('a')] -= 1
            l+=1
            r+=1
            if r >= len(s2):
                break
            candidate[ord(s2[r])-ord('a')] += 1

        return False


