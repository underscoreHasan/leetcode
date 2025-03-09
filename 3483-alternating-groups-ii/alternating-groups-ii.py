class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        #01010 => 010, 101, 010, 100, 001 k = 3
        #0100101 => 010010,100101,001010,010101,101010,010100,101001,010010
        #1101 => 1101         
        l, r = 0, 1
        res = 0
        colors.extend(colors[:k-1])

        while r < (len(colors)):
            if (colors[r-1] != colors[r]): #checking alternation
                if (r - l + 1) == k:
                    res += 1
                    l += 1
                r += 1
            else:
                l = r
                r += 1

        return res

