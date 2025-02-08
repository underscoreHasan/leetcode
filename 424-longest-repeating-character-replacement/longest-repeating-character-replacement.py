class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #XYYX k = 2 -> YYYY, XXXX
        #AAABABB -> AAAAABB, AAABBBB wrong
        #ABBB k=2 -> BBBB
        l = r = 0
        counts = {}
        res = 0

        while r < len(s):
            counts[s[r]] = 1 + counts.get(s[r], 0)

            #make sure that current window is valid
            #it is valid when the window only requires a max of k replacements
            #if vs while?
            if ((r-l+1) - max(counts.values())) > k:
                counts[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)
            r+=1
        
        return res



            