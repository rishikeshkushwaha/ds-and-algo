import pandas as pd
import numpy as np

# file1 = open("a_an_example.in.txt","r")
with open("e_elaborate.in.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
clients = lines[0]

client_data = {}

like_items = []
dislike_items = []


for i in range(1, int(clients)+1):
    client_data[(i, 'like')] = lines[2*i-1].split(' ')
    client_data[(i, 'dislike')] = lines[2*i].split(' ')
    like_items.append(lines[2*i-1].split(' '))
    dislike_items.append(lines[2*i].split(' '))

like_int, like_str = [], []
for x in (set([_ for i in like_items for _ in i ])):
    try:
        like_int.append(int(x))
    except ValueError:
        like_str.append(x)
dislike_int, dislike_str = [], []
for x in (set([_ for i in dislike_items for _ in i ])):
    try:
        dislike_int.append(int(x))
    except ValueError:
        dislike_str.append(x)
# print(len(set(like_str)-set(dislike_str)), set(like_str)-set(dislike_str) )
file1 = open('output_e.txt', 'w')

ans = list(set(like_str)-set(dislike_str))
ans_str = str(len(ans))+' '
for i in ans:
    ans_str = ans_str + i+' '
file1.writelines(ans_str)
