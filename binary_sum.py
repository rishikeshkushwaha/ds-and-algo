# 67. Add Binary

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ''
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or carry == 1:
            s = carry
            if i >= 0:
                s += int(a[i])
                i -= 1
            if j >= 0:
                s += int(b[j])
                j -= 1
            result += str(s % 2)
            carry = s // 2
        return result[::-1]


s = Solution()
a = '1'
b = '11'
print(s.addBinary(a, b))
