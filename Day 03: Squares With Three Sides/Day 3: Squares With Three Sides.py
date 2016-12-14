#!/usr/local/bin/python3

def read_input_moves(filename):
    content = []
    with open(filename) as input_file:
        for lines in input_file:
            content.append(lines)
    return content

class Triangle:

    def __init__(self, sides_list):
        sides_list.sort()
        self.short_side, self.mid_side, self.long_side = sides_list

    def isvalid(self):
        return ((self.short_side + self.mid_side) > self.long_side)


INPUT = (read_input_moves('./input'))
# read the input file into a list

def star1(triangle_list):
    int_sides_list = []
    for sides_list in triangle_list:
        int_sides_list.append([int(i) for i in sides_list.split()])

    valid_triangles = []
    for triangle_sides in int_sides_list:
        triangle = Triangle(triangle_sides)
        if triangle.isvalid():
            valid_triangles.append(sides_list)
    return len(valid_triangles)


print("Star 1: ", star1(INPUT))


def rotate_3x3(three_element_list):
    return [ list(x) for x in zip(*three_element_list) ]


def star2(triangle_list):
    int_sides_list = []
    for sides_list in triangle_list:
        int_sides_list.append([int(i) for i in sides_list.split()])

    new_sides_list = []
    while (len(int_sides_list) % 3 == 0) and (len(int_sides_list) > 0):
        rot_list = [int_sides_list.pop(0), int_sides_list.pop(0), int_sides_list.pop(0)]
        new_sides_list.extend(rotate_3x3(rot_list))

    valid_triangles = []
    for triangle_sides in new_sides_list:
        triangle = Triangle(triangle_sides)
        if triangle.isvalid():
            valid_triangles.append(sides_list)
    return len(valid_triangles)


print("Star 2: ", star2(INPUT))