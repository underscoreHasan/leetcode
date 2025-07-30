class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        currChars = set()
        longestSubStr = 0

        while r< len(s):
            if s[r] in currChars:
                longestSubStr = max(longestSubStr, r-l)
                currChars.remove(s[l])
                l += 1
            else:
                currChars.add(s[r])
                r+=1

        return max(longestSubStr, r-l)
            

