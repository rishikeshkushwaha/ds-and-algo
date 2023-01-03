# 944. Delete Columns to Make Sorted
from typing import List
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        del_col = 0
        for i in range(len(strs[0])):
            new_str = [s[i] for s in strs]
            if sorted(new_str)!=new_str:
                del_col+=1
        return del_col

s = Solution()
strs = ["cba","daf","ghi"]
print(s.minDeletionSize(strs))