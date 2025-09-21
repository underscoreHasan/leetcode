class Solution:
    def myAtoi(self, s: str) -> int:
        res = ""
        digitRead = False
        
        for c in s:
            # step 1: skip leading spaces
            if c == " ":
                if not res:  # haven’t started reading yet
                    continue
                else:  # stop if we already started
                    break
            
            # step 2: handle signs
            if c in ["-", "+"]:
                if not res:  # only allowed at the start
                    res += c
                    continue
                else:
                    break

            # step 3: handle digits
            if c.isdigit():
                res += c
                digitRead = True
            else:
                break

        # step 4: convert to int safely
        if digitRead:
            try:
                num = int(res)
            except ValueError:
                return 0  # just in case

            # clamp result
            if num >= 2**31 - 1:
                return 2**31 - 1
            elif num < -2**31:
                return -2**31
            else:
                return num
        else:
            return 0