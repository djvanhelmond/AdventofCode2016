#!/usr/local/bin/python3
import numpy
import ShortestPath as spf


class BunnyOffice():
    def __init__(self, height, width, dfn):
        self.height = height
        self.width = width
        self.dfn = dfn
        self.layout = numpy.zeros((self.height, self.width), dtype=bool)
        for i in range(self.height):
            for j in range(self.width):
                self.layout[i,j] = self.__is_open_space(j,i) # i, j reversed because numpy has a rotated layout
        self.G = {}
        self.__build_graph()


    def __is_open_space(self, x, y):
        n = (x*x + 3*x + 2*x*y + y + y*y) + self.dfn
        return sum([ int(x) for x in list(bin(n)[2:]) ]) % 2 == 0


    def __build_graph(self):
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



def star1():
    DESIGNERS_FAVORITE_NUMBER = 1362
    START = "1,1"
    END = "39,31"

    b_office = BunnyOffice(40, 40, DESIGNERS_FAVORITE_NUMBER)
#    b_office.show(spf.shortestPath(b_office.G, START, END))
    return len(spf.shortestPath(b_office.G, START, END))-1

if __name__ == '__main__':
    print("Star 1: ", star1())

