class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [True for i in range(right+1)]
        sieve[0] = sieve[1] = False
        p = 2
        closest = [-1,-1]
        mindiff = float("inf")

        while (p*p <= right):
            if (sieve[p] == True):
                for i in range(p*p, right+1, p):
                    sieve[i] = False
            p += 1
        
        primes = [i for i in range(left, right + 1) if sieve[i]]

        if len(primes) < 2:
            return [-1,-1]
        
        for i in range(1, len(primes)):
            diff = primes[i] - primes[i-1]
            if diff < mindiff:
                mindiff = diff
                closest = [primes[i-1], primes[i]]

        return closest