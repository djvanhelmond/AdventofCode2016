#!/usr/local/bin/python3
import hashlib
import ShortestPath as spf


def hash_key(value):
    md5hash = hashlib.md5()
    md5hash.update(value.encode())
    return md5hash.hexdigest()


class SecureVault():
    def __init__(self, passcode):
        self.passcode = passcode
        self.start_room = [1, 1]
        self.possible_path_to_vault = []
        self.G = {}
        self.__build_graph("")

    def __open_doors(self, path):
        lockstate = hash_key(self.passcode+path)[0:4]
        open_doors = []
        if lockstate[0] in "bcdef": open_doors.append("U")
        if lockstate[1] in "bcdef": open_doors.append("D")
        if lockstate[2] in "bcdef": open_doors.append("L")
        if lockstate[3] in "bcdef": open_doors.append("R")
        return ''.join(open_doors)

    def __path_is_in_bounds(self, path):
        current_room = list(self.start_room)
        for char in path:
            if char == "U": current_room[1] -= 1
            if char == "D": current_room[1] += 1
            if char == "L": current_room[0] -= 1
            if char == "R": current_room[0] += 1

            if (current_room[0] < 1) or (current_room[0] > 5):
                return False
            if (current_room[1] < 1) or (current_room[1] > 5):
                return False
        return True

    def __room_is_vault(self, path):
        current_room = list(self.start_room)
        for char in path:
            if char == "U": current_room[1] -= 1
            if char == "D": current_room[1] += 1
            if char == "L": current_room[0] -= 1
            if char == "R": current_room[0] += 1
        if current_room == [4, 4]:
            return True
        return False

    def __build_graph(self, path):
        if len(path) < 50:
            self.G[path] = {}
            for i in self.__open_doors(path):
                if self.__path_is_in_bounds(path+i):
                    self.G[path][path+i] = 1
            for potential_path in self.G[path]:
                if not self.__room_is_vault(potential_path):
                    self.__build_graph(potential_path)
                else:
                    self.possible_path_to_vault.append(potential_path)


def star1(passcode):
    sv = SecureVault(passcode)
    return min(sv.possible_path_to_vault, key=len)


if __name__ == '__main__':
    PASSCODE = "gdjjyniy"
    print("Star 1: ", star1(PASSCODE))
#    print("Star 2: ", star2())

