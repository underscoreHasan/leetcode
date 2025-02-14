class ProductOfNumbers:

    def __init__(self):
        self.stream = []
        self.prefixMult = [1]

    def add(self, num: int) -> None:
        self.stream.append(num)
        # if not self.prefixMult:
        #     self.prefixMult.append(num)
        if not num:
            self.prefixMult = [1]
        else:
            self.prefixMult.append(self.prefixMult[-1] * num)

    def getProduct(self, k: int) -> int:
        return 0 if (k+1 > len(self.prefixMult)) else int(self.prefixMult[-1] / self.prefixMult[-k-1])

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
