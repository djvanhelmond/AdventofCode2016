#!/usr/local/bin/python3


class Disc():
    def __init__(self, disc_id, tot_pos, init_pos):
        self.id = disc_id
        self.total_positions = tot_pos
        self.current_position = init_pos

    def is_open(self):
        return (self.current_position + self.id) % self.total_positions == 0


class Kinetic_Sculpture():
    def __init__(self):
        self.all_discs = []
        self.time = 0

    def configure_disc(self, disc_settings):
        self.all_discs.append(Disc(*disc_settings))

    def tick(self):
        self.time += 1
        for disc in self.all_discs:
            disc.current_position = (disc.current_position + 1) % disc.total_positions


def run(setup):
    # creating a kinetic sculpture
    ks = Kinetic_Sculpture()
    # setting all disks to their initial input (puzzle input)
    for i in range(len(setup)):
        ks.configure_disc(setup[i])
    #while not all disks are open at the right moment
    while not all([disc.is_open() for disc in ks.all_discs]):
        # increase the time by 1 second
        ks.tick()
    # return me the right time
    return ks.time


if __name__ == '__main__':
    DISK_SETUP = [[1, 17, 15], [2, 3, 2], [3, 19, 4], [4, 13, 2], [5, 7, 2], [6, 5, 0]]
    print("Star 1: ", run(DISK_SETUP))
    DISK_SETUP = [[1, 17, 15], [2, 3, 2], [3, 19, 4], [4, 13, 2], [5, 7, 2], [6, 5, 0], [7, 11, 0]]
    print("Star 2: ", run(DISK_SETUP))

