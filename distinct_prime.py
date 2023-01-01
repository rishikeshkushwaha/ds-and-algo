class Solution(object):
    def distinctPrimeFactors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product = max(nums)
        if product == 2:
            return 1
        primes = [True] * (product+1)
        if product < 2:
            return 0
        primes[0], primes[1] = 0, 0
        for i in range(2, int(product ** 0.5) + 1):
            if primes[i]:
                for j in range(i + i, product, i):
                    primes[j] = 0
        primes = [i for i, v in enumerate(primes) if v == True]
        ans = []
        while product != 1:
            for i in primes:
                while product % i == 0:
                    product = product / i
                    ans.append(i)
        return len(set(ans))


s = Solution()
nums = [3]
print(s.distinctPrimeFactors(nums))
