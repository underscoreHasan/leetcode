class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''

        def expandFromCenter(l,r):
            while r < len(s) and l>=0 and s[l] == s[r]:
                l -= 1
                r += 1
            nonlocal res
            res = res if len(res) > len(s[l+1:r]) else s[l+1:r]
        
        for i in range(len(s)):
            expandFromCenter(i,i)
            expandFromCenter(i,i+1)

        return res