class Solution:
    def coloredCells(self, n: int) -> int:
      # 1, 1+4 = 5, 1+4+8 = 13, 1+4+8+12= 25
      #a + (n-1)d
      #n(2a+(n-1)d)/2
      #4,8,12,16,20


        # if n>1:
        #     res += int((n-1)*(2*4))

        return 1+int((n-1)*(2*4+(n-2)*4)/2)