class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
            # if n (power of x) is negative change x to 1/x and make n positive
        if n < 0:
            x = 1 / x
            n = -n
            # the updated x and n will be sent further
        return x * pow(x, n - 1)


s = Solution()
x = .00002
n = 2323235645
print(s.myPow(x, n))
