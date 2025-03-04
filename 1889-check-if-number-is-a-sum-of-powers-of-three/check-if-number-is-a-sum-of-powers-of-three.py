import math

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        #1, 3, 9, 27, 81, 243, 729
        #12 = 3^2 3^1 Greedy works
        #91 = 3^4 3^2 3^0 Greedy works
        #21 = 3^2 3^1 3^0 greedy works, but failure

        j = int(math.log(n, 3))

        for i in range(j, -1, -1):
            if n >= 3**i:
                n -= 3**i
            if n == 0:
                return True

        return False
        