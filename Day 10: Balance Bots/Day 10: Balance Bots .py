#!/usr/local/bin/python3

class Bot():
    def __init__(self, bot_id, next_low, next_high):
        self.bot_id = bot_id
        self.next_low = next_low
        self.next_high = next_high
        self.values = [None, None]
        self.is_actionable = False

    def add_value(self, value):
        if self.values[0] == None:
            self.values[0] = value
        else:
            self.values[1] = value
            self.is_actionable = True

    def execute(self):
        self.is_actionable = False
        if self.next_low[0] == 'bot':
            bots[self.next_low[1]].add_value(min(self.values))
        else:
            outputs[self.next_low[1]]=min(self.values)
        if self.next_high[0] == 'bot':
            bots[self.next_high[1]].add_value(max(self.values))
        else:
            outputs[self.next_high[1]]=max(self.values)


def read_input_moves(filename):
    content = []
    with open(filename) as input_file:
        for lines in input_file:
            content.append(lines)
    return content
INPUT = (read_input_moves('./input'))

def star1():
    for n in bots:
        if (min(bots[n].values) == 17) and (max(bots[n].values) == 61):
            return bots[n].bot_id

def star2():
    return outputs[0]*outputs[1]*outputs[2]


if __name__ == '__main__':

    # build a list with all the bots
    bots = {}
    for line in INPUT:
        if line.split()[0] == 'bot':
            b_id = int(line.split()[1])
            low = ((line.split()[5]), int(line.split()[6]))
            high = ((line.split()[10]), int(line.split()[11]))
            bots[b_id]=Bot(b_id, low, high)

    # hand out all the input values to the bots
    for line in INPUT:
        if line.split()[0] == 'value':
            bots[int(line.split()[5])].add_value(int(line.split()[1]))

    # while any bot still has values to process, repeat the execution-loop
    outputs = {}
    while any([bots[n].is_actionable for n in range(len(bots))]):
        for n in range(len(bots)):
            if bots[n].is_actionable:
                bots[n].execute()

    # return the output required
    print("Star 1 - bot number: ", star1())
    print("Star 2 - output values: ", star2())






