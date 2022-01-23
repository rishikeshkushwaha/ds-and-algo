class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        a, mi, ma = 0, 0, 0
        for d in differences:
            a +=d
            ma = max(ma, a)
            mi = min(mi, a)
        if ma-mi > upper-lower:
            return 0
        return (upper-lower)-(ma-mi) + 1

sol = Solution()
numbers = [3,-4,5,1,-2]
lower= -4
upper=5
print(sol.numberOfArrays(differences=numbers,lower=lower,upper=upper))