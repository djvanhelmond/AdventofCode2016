#!/usr/local/bin/python3
import numpy
import ShortestPath as spf


class BunnyOffice():
    def __init__(self, height, width, dfn):
        self.G = {}
        self.dfn = dfn
        self.height = height
        self.width = width
        self.layout = numpy.zeros((self.height, self.width), dtype=bool)
        for i in range(self.height):
            for j in range(self.width):
                self.layout[i,j] = self.is_open_space(j,i) # i, j reversed because numpy has a rotated layout
        self.build_graph()


    def show(self, path = [""]):
        line = ["  "]
        for i in range(self.width):
            line.append(str(i)[-1])
        print(''.join(line))
        for i in range(self.height):
            line = [str(i)[-1], " "]
            for j in range(self.width):
                if str(i) + "," + str(j) in path:
                    line.append("O")
                else:
                    if self.layout[i, j]:
                        line.append(".")
                    else:
                        line.append("#")
            print(''.join(line))


    def is_open_space(self, x, y):
        n = (x*x + 3*x + 2*x*y + y + y*y) + self.dfn
        return sum([ int(x) for x in list(bin(n)[2:]) ]) % 2 == 0


    def build_graph(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.layout[i,j]:
                    self.G[str(i)+","+str(j)] = {}
                    if (i-1 >= 0):
                        if self.layout[i-1,j]:
                            self.G[str(i)+","+str(j)][str(i - 1)+","+str(j)] = 1
                    if (i+1 < self.height):
                        if self.layout[i+1,j]:
                            self.G[str(i)+","+str(j)][str(i + 1) + "," + str(j)] = 1
                    if (j-1 >= 0):
                        if self.layout[i,j-1]:
                            self.G[str(i)+","+str(j)][str(i) + "," + str(j - 1)] = 1
                    if (j+1 < self.width):
                        if self.layout[i,j+1]:
                            self.G[str(i)+","+str(j)][str(i) + "," + str(j + 1)] = 1


def star1():
    start = "1,1"
    end = "39,31"
#    m.show(spf.shortestPath(m.G, start, end))
    return len(spf.shortestPath(m.G, start, end))-1

if __name__ == '__main__':
    DESIGNERS_FAVORITE_NUMBER = 1362
    m = BunnyOffice(40, 40, DESIGNERS_FAVORITE_NUMBER)
    print("Star 1: ", star1())

