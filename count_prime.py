# 204. Count Primes

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [True]*n
        if n < 2:
            return 0
        primes[0], primes[1] = False, False
        for i in range(2, int(n**0.5)+1):
            if primes[i]:
                for j in range(i+i,n,i):
                    primes[j] = False
        return sum(primes)


s = Solution()
n = 10
print(s.countPrimes(n))
