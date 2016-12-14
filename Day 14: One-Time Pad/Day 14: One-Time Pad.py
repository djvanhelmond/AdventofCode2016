#!/usr/local/bin/python3
import hashlib


#SALT = "abc"
SALT = "cuanljph"


class OTP():
    def __init__(self, salt):
        self.salt = salt
        self.counter = -1
        self.current_key = ""
        self.candidate_keys = []
        self.valid_keys = []

    def __gen_next_key(self):
        md5hash = hashlib.md5()
        md5hash.update((self.salt + str(self.counter)).encode())
        self.current_key = md5hash.hexdigest()

    def __gen_next_stretched_key(self):
        md5hash = hashlib.md5()
        self.current_key = (self.salt + str(self.counter))
        for i in range(2017):
            md5hash = hashlib.md5()
            md5hash.update(self.current_key.encode())
            self.current_key = md5hash.hexdigest()

    def __purge_old_candidates(self):
        delete_list = []
        for candidate_key in self.candidate_keys:
            if candidate_key[0]+1000 <= self.counter:
               delete_list.append(candidate_key)
        self.candidate_keys = [x for x in self.candidate_keys if x not in delete_list]

    def __eval_if_candidate_key(self):
        for i in range(len(self.current_key)-2):
            if self.current_key[i]*3 == self.current_key[i:i+3]:
                self.candidate_keys.append([self.counter, self.current_key, self.current_key[i]])
                return None

    def __eval_if_valid_key(self):
        delete_list = []
        for n in self.candidate_keys:
            if n[0] != self.counter:
                if n[2]*5 in self.current_key:
#                    print("%i FOUND Index: %i Hash: %s match with %s" %
#                            (len(self.valid_keys),self.counter,self.current_key ,n))
                    self.valid_keys.append(n)
                    delete_list.append(n)
        self.candidate_keys = [x for x in self.candidate_keys if x not in delete_list]

    def run(self, star):
        while len(self.valid_keys) < 63:
            self.counter += 1
            if star == 1:
                self.__gen_next_key()
            elif star == 2:
                self.__gen_next_stretched_key()
            self.__purge_old_candidates()
            self.__eval_if_candidate_key()
            self.__eval_if_valid_key()


def star(star):
    onetimepad = OTP(SALT)
    onetimepad.run(star)
    return onetimepad.valid_keys[63][0] # key 63 is the 64th key, [0] is the key index

if __name__ == '__main__':
    print("Star 1: ", star(1))
    print("Star 2: ", star(2))


