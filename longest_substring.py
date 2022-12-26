class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        for i in range(len(s)):
            m, current_length, = [], 0
            for j in range(i, len(s)):
                if s[j] not in m:
                    m.append(s[j])
                    current_length += 1
                else:
                    break
            if current_length > max_length:
                max_length = current_length
        return max_length


s = Solution()
string = "pwwkew"
print(s.lengthOfLongestSubstring(string))
