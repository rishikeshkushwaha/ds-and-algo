class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            elif people[right] <= limit < people[right]+people[left]:
                right -= 1
            boats += 1
        return boats

s = Solution()
people = [3,5,3,4]
limit = 5
print(s.numRescueBoats(people=people, limit=limit))
