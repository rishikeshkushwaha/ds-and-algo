class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        for i in s:
            try:
                d[i] += 1
            except KeyError:
                d[i] = 1
        d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        s = ''
        for k, v in d:
            s += k * v
        return s


s = Solution()
ans = s.frequencySort("tree")
print(ans)
