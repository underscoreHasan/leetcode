class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        #01010 => 010, 101, 010, 100, 001 k = 3
        #0100101 => 010010,100101,001010,010101,101010,010100,101001,010010
        #1101 => 1101         
        l, r = 0, 1
        res = 0
        colors.extend(colors[:k-1])

        while r < (len(colors)): #while right is less than length, meaning that we have more subarrays to check
            if (colors[r-1] != colors[r]): #checking alternation
                if (r - l + 1) == k: #if the required window size is met
                    res += 1 #increase the res by 1
                    l += 1 #move the l pointer
                r += 1 #move the right pointer if alternation holds
            else: #alternation failed
                l = r #skip l pointer ahead
                r += 1 #increase window size to 1

        return res

