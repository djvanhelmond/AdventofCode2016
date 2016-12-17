#!/usr/local/bin/python3


class Disc():
    def __init__(self, input):
        self.data = input[0]
        self.length = input[1]
        while len(self.data) < self.length:
            self.__gen_dragon_curve()
        self.data = self.data[0:self.length]
        self.checksum = self.__gen_checksum(self.data)

    def __gen_dragon_curve(self):
        a = self.data
        b = self.data[::-1].replace("0", "#").replace("1", "0").replace("#", "1")
        self.data = a + "0" + b

    def __gen_checksum(self, data):
        cs = []
        for i in range(0, len(data), 2):
            if data[i] == data[i+1]:
                cs.append("1")
            else:
                cs.append("0")
        if len(cs) % 2 == 0:
            cs = self.__gen_checksum(cs)
        return ''.join(cs)



def star1(INPUT):
    disk = Disc(INPUT)
    return disk.checksum

if __name__ == '__main__':
    INPUT = ("11110010111001001", 272)
    print("Star 1: ", star1(INPUT))
    INPUT = ("11110010111001001", 35651584)
    print("Star 2: ", star1(INPUT))






