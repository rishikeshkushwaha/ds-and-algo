class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        ans = 0
        max_time = min(time)*totalTrips
        while ans <= totalTrips:
            for i in range(1, max_time):
                ans = sum([int(i/t) for t in time if t<=i and i%t==0])
        return ans


sol = Solution()
time= [1,2,3]
totalTrips =5
print(sol.minimumTime(time,totalTrips))