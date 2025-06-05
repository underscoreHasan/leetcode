class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # abcabcbb => abc 3
        # BBBBB => bbbbb 1
        # pwwke => wke

        res = 0

        l, r = 0, 0

        curr = set()

        while r < len(s):
            if s[r] not in curr: # if letter not in dict
                curr.add(s[r])
                r+=1
                res = max(res, r-l)
            else: # if already seen
                curr.remove(s[l])
                l+=1
        
        return res
