class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """

        def minutes(time):
            h = int(time.split(":")[0]) * 60
            m = int(time.split(":")[1])
            return h + m

        current = minutes(current)
        correct = minutes(correct)
        ans = 0
        while current != correct:
            diff = abs(correct - current)
            if diff >= 60:
                current += int(diff / 60) * 60
                ans += int(diff / 60)
            elif 15 <= diff < 60:
                current += int(diff / 15) * 15
                ans += int(diff / 15)

            elif 5 <= diff < 15:
                current += int(diff / 5) * 5
                ans += int(diff / 5)

            else:
                current += int(diff)
                ans += int(diff)
        return ans

s = Solution()
current = "02:30"
correct = "04:35"
print(s.convertTime(current, correct))