class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        product = right+1
        primes = [True] * (product+1)
        if product < 2:
            return 0
        primes[0], primes[1] = 0, 0
        for i in range(2, int(product ** 0.5) + 1):
            if primes[i]:
                for j in range(i + i, product, i):
                    primes[j] = 0
        # print(primes)
        primes = [i for i, v in enumerate(primes) if v == True and i>=left and i<=right]
        # print(primes)
        ans ={}
        for i,j in zip(primes[:-1],primes[1:]):
            ans[(i,j)] = j-i
        # print(ans)
        return min(ans.items(), key=lambda x: x[1])[0]
s = Solution()
left = 10

right  = 19
print(s.closestPrimes(left,right))
