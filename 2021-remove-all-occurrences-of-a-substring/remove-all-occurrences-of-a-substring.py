class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        #da abc baabcbc =dab
        #daba abc bc
        #dababc
        #axxxxyyyyb
        #axxxyyyb

        c = 0
        w = len(part)
        
        while c < len(s):
            if s[c:c + w] == part:
                s = s[:c] + s[c+w:]
                c = 0
                continue
            c+=1
        
        return s
                
        