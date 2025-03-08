class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r = 0, k
        s = blocks[:r]
        sCount = Counter(s)
        minW = sCount['W']

        while r < len(blocks):
            sCount[blocks[r]] += 1
            sCount[blocks[l]] -= 1
            l+=1
            r+=1
            minW = min(minW, sCount['W'])

        return minW



            

        