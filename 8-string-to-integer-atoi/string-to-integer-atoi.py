class Solution:
    def myAtoi(self, s: str) -> int:
        res = ""
        digitRead = False
        for c in s:
            #step 1
            if c == " ":
                if not res:
                    continue
                else:
                    break
            
            #step 2
            if c in ["-", "+"]:
                if not res:
                    res += c
                    continue
                else:
                    break

            #step 3
            if str.isdigit(c):
                res += (c)
                digitRead = True
            else:
                break

        if digitRead:
            res = int(res)
            if res >= 2**31 -1:
                return 2**31 -1
            elif res < -2**31:
                return -2**31
            else:
                return res
        else:
            return 0    


            

            
