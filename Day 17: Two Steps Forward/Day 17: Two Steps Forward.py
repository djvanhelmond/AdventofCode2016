#!/usr/local/bin/python3
import hashlib


def hash_key(value):
    md5hash = hashlib.md5()
    md5hash.update(value.encode())
    return md5hash.hexdigest()


class SecureVault():
    def __init__(self, passcode):
        self.__passcode = passcode
        self.__start_room = [1, 1]
        self.__possible_path_to_vault = []
        self.__G = {}
        self.__build_graph("")

    def __open_doors(self, path):
        lockstate = hash_key(self.__passcode+path)[0:4]
        open_doors = []
        if lockstate[0] in "bcdef": open_doors.append("U")
        if lockstate[1] in "bcdef": open_doors.append("D")
        if lockstate[2] in "bcdef": open_doors.append("L")
        if lockstate[3] in "bcdef": open_doors.append("R")
        return ''.join(open_doors)

    def __path_is_in_bounds(self, path):
        current_room = list(self.__start_room)
        for char in path:
            if char == "U": current_room[1] -= 1
            if char == "D": current_room[1] += 1
            if char == "L": current_room[0] -= 1
            if char == "R": current_room[0] += 1
            if (current_room[0] < 1) or (current_room[0] > 4) or (current_room[1] < 1) or (current_room[1] > 4):
                return False
        return True

    def __room_is_vault(self, path):
        current_room = list(self.__start_room)
        for char in path:
            if char == "U": current_room[1] -= 1
            if char == "D": current_room[1] += 1
            if char == "L": current_room[0] -= 1
            if char == "R": current_room[0] += 1
        if current_room == [4, 4]:
            return True
        return False

    def __build_graph(self, path):
        self.__G[path] = {}
        for i in self.__open_doors(path):
            if self.__path_is_in_bounds(path+i):
                self.__G[path][path+i] = 1
        for potential_path in self.__G[path]:
            if not self.__room_is_vault(potential_path):
                self.__build_graph(potential_path)
            else:
                self.__possible_path_to_vault.append(potential_path)
        del self.__G[path]

    def return_path_list(self):
        return self.__possible_path_to_vault



def star1(vault):
    return min(vault.return_path_list(), key=len)

def star2(vault):
    return len(max(vault.return_path_list(), key=len))

if __name__ == '__main__':
    PASSCODE = "gdjjyniy"
    sv = SecureVault(PASSCODE)
    print("Star 1: ", star1(sv))
    print("Star 2: ", star2(sv))




