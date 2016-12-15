#!/usr/local/bin/python3

disc_setup = [[1, 17, 15], [2, 3, 2], [3, 19, 4], [4, 13, 2], [5, 7, 2], [6, 5, 0]]
time = 0
while not all([(disc[2] + disc[0] + time) % disc[1] == 0 for disc in disc_setup]): time +=1
print(time)

disc_setup = [[1, 17, 15], [2, 3, 2], [3, 19, 4], [4, 13, 2], [5, 7, 2], [6, 5, 0], [7, 11, 0]]
time = 0
while not all([(disc[2] + disc[0] + time) % disc[1] == 0 for disc in disc_setup]): time +=1
print(time)