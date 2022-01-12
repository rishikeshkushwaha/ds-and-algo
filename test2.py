import math


def find_sqrt(number,list_sq):
    print(list_sq)
    l = 0
    r = len(list_sq)-1
    mid=0
    while l<=r:
        mid=(l+r)//2
        if number*number < list_sq[mid]:
            l= mid+1
        elif number*number > list_sq[mid]:
            r = mid-1
    return mid
number = 44
list_sq = [i*i for i in range(1,int(number/2))]
print(find_sqrt(44,list_sq=list_sq))
