class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        from itertools import permutations
        from collections import Counter
        digi_keys = (Counter(digits))
        print(digits)

        for k, v in digi_keys.items():
            if v > 3:
                digi_keys[k] = 3
        print(digi_keys)
        d=[]
        for k,v in digi_keys.items():
            d.append([k]*v)
        d = [j for sub in d for j in sub]
        # print(d)
        # exit(0)
        # Get all permutations of length 2
        # and length 2
        ans = []
        perm = permutations(d, 3)
        for i in perm:
            if (i[0] * 100 + i[1] * 10 + i[2]) % 2 == 0 and (i[0] * 100 + i[1] * 10 + i[2]) > 99:
                ans.append(i[0] * 100 + i[1] * 10 + i[2])

        # ans=[]
        # for i in range(len(digits)):
        #     for j in range(i+1,len(digits)):
        #         for k in range(+1,len(digits)):
        #             print(digits[i]*100+digits[j]*10+digits[k])
        #             if (digits[i]*100+digits[j]*10+digits[k]) %2 ==0:
        #                 ans.append(digits[i]*100+digits[j]*10+digits[k])

        return sorted(set(ans))


sol = Solution()
digits = [2,2,8,8,2]
print(sol.findEvenNumbers(digits))




