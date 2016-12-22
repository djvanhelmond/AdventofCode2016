#!/usr/local/bin/python3
import ShortestPath as spf


class StorageNode():
    def __init__(self, size, used, avail):
        self.size = int(size)
        self.used = int(used)
        self.avail = int(avail)
        self.heavy = False


class GridStorage():
    def __init__(self, df_file):
        self.nodes = {}
        with open(df_file) as input_file:
            for line in input_file:
                if "/dev/grid/node" in line:
                    X, Y, size, used, avail = line.replace("/dev/grid/node-","").replace("x","").replace("y","").replace("-"," ").replace("T","").split()[0:5]
                    self.nodes[(int(X),int(Y))] = StorageNode(size,used,avail)
        self.viable_pairs = 0
        self.__viable_pairs()
        self.G = {}
        self.__build_graph()

    def __build_graph(self):
        for node_A in self.nodes:
            self.G[node_A] = {}
            for node_B in self.nodes:
                if not ((node_A == node_B) or self.nodes[node_A].heavy or self.nodes[node_B].heavy):
                    if (abs(node_A[0] - node_B[0]) + abs(node_A[1] - node_B[1]) <= 1):
                        self.G[node_A][node_B] = 1

    def __viable_pairs(self):
        for node_A in self.nodes:
            for node_B in self.nodes:
                if (self.nodes[node_A].used != 0) and (node_A != node_B) and (self.nodes[node_A].used <= self.nodes[node_B].avail):
                    self.viable_pairs += 1
                if (self.nodes[node_A].used == 0) and (self.nodes[node_A].avail <= self.nodes[node_B].used):
                    self.nodes[node_B].heavy = True

    def star2(self):
        goal_node = ((max([ x for x,y in self.nodes if y is 0 ])),0)
        empty_node = [ node for node in self.nodes if self.nodes[node].used == 0 ][0]
        steps = len(spf.shortestPath(self.G, empty_node, goal_node)) - 2
        return (((goal_node[0]-1) * 5) + 1 + steps)


if __name__ == '__main__':
    gs = GridStorage("./input")
    print("Star 1: ", gs.viable_pairs)
    print("Star 2: ", gs.star2())






