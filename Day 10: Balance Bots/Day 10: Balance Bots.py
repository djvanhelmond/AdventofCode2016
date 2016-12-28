#!/usr/local/bin/python3

def read_input_moves(filename):
    return open(filename).readlines()


class Bot():
    """
    Bots are zooming around handing small microchips to each other. Each bot only proceeds when
    it has two microchips, and once it does, it gives each one to a different bot or puts it in
    a marked "output" bin. Sometimes, bots take microchips from "input" bins, too.

    Some of the instructions specify that a specific-valued microchip should be given to a
    specific bot; the rest of the instructions indicate what a given bot should do with its
    lower-value or higher-value chip.
    """

    def __init__(self, bot_id, next_low, next_high):
        """
        When a new bot gets instantiated, it needs its instructions set
        :param bot_id:      The ID of the Bot
        :param next_low:    The action that it should do with the low value. Tuple, e.g. (bot, 34)
        :param next_high:   The action that it should do with the high value. Tuple, e.g. (output, 7)
        """
        self.bot_id = bot_id
        self.next_low = next_low
        self.next_high = next_high
        self.microchips = []            # List that can contain up to two microchips
        self.is_actionable = False      # When the bot has exactly two microchips, it can be processed

    def add_microchips(self, microchip):
        """
        Function to give a microchip to a bot. The microchip gets added to the list
        """
        self.microchips.append(microchip)
        if len(self.microchips) == 2:   # when the bot has exactly two microchips, it can be processed
            self.is_actionable = True

    def execute(self):
        """
        When the bot has exactly two microchips, it will be actionable and the action can be executed.
        The bot will give the microchips either to het next bot or put the microchip in the output.
        """
        self.is_actionable = False
        if self.next_low[0] == 'bot':
            bots[self.next_low[1]].add_microchips(min(self.microchips))
        else:
            outputs[self.next_low[1]]=min(self.microchips)
        if self.next_high[0] == 'bot':
            bots[self.next_high[1]].add_microchips(max(self.microchips))
        else:
            outputs[self.next_high[1]]=max(self.microchips)


def star1():
    for n in bots.keys():
        if (min(bots[n].microchips) == 17) and (max(bots[n].microchips) == 61):
            return bots[n].bot_id

def star2():
    return outputs[0]*outputs[1]*outputs[2]


if __name__ == '__main__':
    # read all instructions into the INPUT list
    INPUT = (read_input_moves('./input'))

    # first time, read all lines that contain instruction to setup bots
    bots = {}   # a dict that will contain all the bots, with their instructions loaded
    outputs = {} # a dict that will contain all the outputs

    for line in INPUT:
        if line.split()[0] == 'bot':
            b_id = int(line.split()[1])                         # assign Bot_ID
            low = ((line.split()[5]), int(line.split()[6]))     # setup "low" instruction
            high = ((line.split()[10]), int(line.split()[11]))  # setup "high" instruction
            bots[b_id]=Bot(b_id, low, high)                     # add the bot to the Bots dictionary

    # second time, read all lines that contain instruction to setup input microchips
    for line in INPUT:
        if line.split()[0] == 'value':
            bots[int(line.split()[5])].add_microchips(int(line.split()[1]))

    # at this moment the bots{} dict contains all the bots with their instructions and input
    # microchips loaded

    # with all the input microchips loaded, there must now be bots that are actionable (i.e. have
    # enough microchips to hand them over to the next bot).
    # this loop will keep running as long as there are bots that have enough microchips.
    while any([bots[n].is_actionable for n in bots.keys()]):
        for n in bots.keys():
            if bots[n].is_actionable:
                bots[n].execute()

    # return the output required
    print("Star 1 - bot number: ", star1())
    print("Star 2 - output microchips: ", star2())






