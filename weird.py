num = int(input(""))
ans = []
while num != 1:
    if num % 2 == 0:
        ans.append(num)
        num = num / 2
    else:
        ans.append(num)
        num = num * 3 + 1
ans.append(1)
for i in ans:
    print(int(i), end=" ")
