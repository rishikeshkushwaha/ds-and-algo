# 49. Group Anagrams

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map_list = {}
        for s in strs:
            key = ''.join(sorted(s))
            try:
                map_list[key].append(s)
            except KeyError:
                map_list[key] = [s]
        return list(map_list.values())

s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(strs))