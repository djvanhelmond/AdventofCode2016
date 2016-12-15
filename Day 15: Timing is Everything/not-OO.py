#!/usr/local/bin/python3

S = [[1, 17, 15], [2, 3, 2], [3, 19, 4], [4, 13, 2], [5, 7, 2], [6, 5, 0]]
t = 0
while not all([(d[2] + d[0] + t) % d[1] == 0 for d in S]): t +=1
print(t)

S = [[1, 17, 15], [2, 3, 2], [3, 19, 4], [4, 13, 2], [5, 7, 2], [6, 5, 0], [7, 11, 0]]
t = 0
while not all([(d[2] + d[0] + t) % d[1] == 0 for d in S]): t +=1
print(t)
