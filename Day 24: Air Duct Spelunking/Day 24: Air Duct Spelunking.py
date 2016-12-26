#!/usr/local/bin/python3
import numpy
import ShortestPath as spf
import itertools


def read_hvac_layout(filename):
    content = []
    with open(filename) as input_file:
        for lines in input_file:
            content.append(list(lines))
    return content


class HVAC():
    def __init__(self, raw_input):
        self.width = (len(raw_input[0]) - 1)
        self.height = len(raw_input)
        self.layout, self.POI = self.__parse_input(raw_input)
        self.G = self.__build_graph()
        self.dv = self.__calc_dv_table()

    def __parse_input(self, raw_input):
        POI = {}
        layout = numpy.zeros((self.height, self.width), dtype=bool)
        for i in range(self.height):
            for j in range(self.width):
                if raw_input[i][j] == "#":
                    layout[i,j] = False
                elif raw_input[i][j] == ".":
                    layout[i,j] = True
                elif raw_input[i][j] in "0123456789":
                    layout[i,j] = True
                    POI[int(raw_input[i][j])] = (i,j)
        return layout, POI

    def __build_graph(self):
        G = {}
        for i in range(self.height):
            for j in range(self.width):
                if self.layout[i, j]:
                    G[(i, j)] = {}
                    if (i - 1 >= 0):
                        if self.layout[i - 1, j]:
                            G[(i, j)][(i - 1, j)] = 1
                    if (i + 1 < self.height):
                        if self.layout[i + 1, j]:
                            G[(i, j)][(i + 1, j)] = 1
                    if (j - 1 >= 0):
                        if self.layout[i, j - 1]:
                            G[(i, j)][(i, j - 1)] = 1
                    if (j + 1 < self.width):
                        if self.layout[i, j + 1]:
                            G[(i, j)][(i, j + 1)] = 1
        return G

    def __calc_dv_table(self):
        hop_length = {}
        for hop in list(itertools.combinations(self.POI, 2)):
            hop_length[hop] = len(spf.shortestPath(self.G, self.POI[hop[0]], self.POI[hop[1]])) - 1
        return hop_length

    def __calc_path_len(self, path):
        return sum([ self.dv[min(path[m], path[m+1]), max(path[m], path[m+1])] for m in range(len(path)-1)])

    def find_shortest_path(self):
        return min([ self.__calc_path_len(path) for path in itertools.permutations(list(self.POI)) if path[0] == 0 ])

    def find_shortest_path_loop(self):
        return min([self.__calc_path_len(path + (0,)) for path in itertools.permutations(list(self.POI)) if path[0] == 0])


def star1(layout):
    hvac = HVAC(layout)
    return hvac.find_shortest_path()

def star2(layout):
    hvac = HVAC(layout)
    return hvac.find_shortest_path_loop()


if __name__ == '__main__':
    INPUT = read_hvac_layout('./input')
    print("Star 1: ", star1(INPUT))
    print("Star 2: ", star2(INPUT))






