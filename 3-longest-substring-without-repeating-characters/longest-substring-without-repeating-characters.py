class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # abcabcbb => abc 3
        # BBBBB => bbbbb 1
        # pwwke => wke

        res = 0

        l, r = 0, 0

        curr = DefaultDict(int)

        while r < len(s):
            if curr[s[r]] == 0: # if letter not in dict
                curr[s[r]] += 1
                r+=1
                res = max(res, r-l)
            else: # if already seen
                curr[s[l]] -= 1
                l+=1
        
        return res
