class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        res = []
        r = 0

        for r in range(len(chars)):
            if l <= r:
                if chars[l]==chars[r]:
                    r += 1
                else:
                    res.append(chars[l])
                    if r-l > 1:
                        res.extend(list(str(r - l)))
                    l = r
        res.append(chars[l])
        if r-l > 1:                        
            res.extend(list(str(r - l)))

        print(res)
        chars[:len(res)] = res
        return len(res)




