#!/usr/local/bin/python3
import numpy
import sfp


class BunnyOffice():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.layout = numpy.zeros((self.height, self.width), dtype=bool)
        for i in range(self.height):
            for j in range(self.width):
                self.layout[i,j] = self.is_open_space(j,i) # i, j reversed because numpy has a rotated layout


    def show(self):
        line = ["  "]
        for i in range(self.width):
            line.append(str(i)[-1])
        print(''.join(line))
        for i in range(self.height):
            line = [str(i)[-1], " "]
            for j in range(self.width):
                if self.layout[i, j]:
                    line.append("#")
                else:
                    line.append(".")
            print(''.join(line))

    def is_open_space(self, x, y):
        n = (x*x + 3*x + 2*x*y + y + y*y) + DESIGNERS_FAVORITE_NUMBER
        return sum([ int(x) for x in list(bin(n)[2:]) ]) % 2 == 1

# Graph
#  G = {'s':{'u':10, 'x':5}, 'u':{'v':1, 'x':2}, 'v':{'y':4}, 'x':{'u':3, 'v':9, 'y':2}, 'y':{'s':7, 'v':6}}

# vertex
# 's':{'u':10, 'x':5}

    def build_graph(self):
        G = {}
        for i in range(self.height):
            for j in range(self.width):
                if not self.layout[i,j]:
                    G[str(i)+","+str(j)] = {}
                    if (i-1 >= 0):
                        if not self.layout[i-1,j]:
                            G[str(i)+","+str(j)][str(i - 1)+","+str(j)] = 1
                    if (i+1 < self.height):
                        if not self.layout[i+1,j]:
                            G[str(i)+","+str(j)][str(i + 1) + "," + str(j)] = 1
                    if (j-1 >= 0):
                        if not self.layout[i,j-1]:
                            G[str(i)+","+str(j)][str(i) + "," + str(j - 1)] = 1
                    if (j+1 < self.width):
                        if not self.layout[i,j+1]:
                            G[str(i)+","+str(j)][str(i) + "," + str(j + 1)] = 1
        return G



#DESIGNERS_FAVORITE_NUMBER = 10
#h = 7
#w = 10
#start = "1,1"
#end = "4,7"

DESIGNERS_FAVORITE_NUMBER = 1362
h = 40
w = 40
start = "1,1"
end = "39,31"

m = BunnyOffice(h, w)
m.show()
G = m.build_graph()
print(G)

print("Shortest Length: ", sfp.Dijkstra(G, start)[0][end])
print("Shortest Path: ", sfp.shortestPath(G, start, end))


