#!/usr/local/bin/python3
import hashlib


SALT = "cuanljph"
#SALT = "abc"


class OTP():
    def __init__(self, salt):
        self.salt = salt
        self.counter = -1
        self.current_key = ""
        self.candidate_keys = []
        self.valid_keys = []

    def __gen_next_key(self):
        self.md5 = hashlib.md5()
        self.current_key = self.md5.update((self.salt + str(self.counter)).encode())

    def __eval_candidate_key(self):
        for i in range(len(self.md5.hexdigest())-2):
            if self.md5.hexdigest()[i] == \
                    self.md5.hexdigest()[i+1] == \
                    self.md5.hexdigest()[i+2]:
                self.candidate_keys.append([self.counter, self.md5.hexdigest(), self.md5.hexdigest()[i]])
                return None

    def __eval_valid_key(self):
        delete_list = []
        for n in self.candidate_keys:
            if n[0]+999 < self.counter:
               delete_list.append(n)
            if n[0] != self.counter:
                for i in range(len(self.md5.hexdigest())-4):
                    if n[2] == self.md5.hexdigest()[i] == \
                            self.md5.hexdigest()[i+1] == \
                            self.md5.hexdigest()[i+2] == \
                            self.md5.hexdigest()[i+3] == \
                            self.md5.hexdigest()[i+4]:
#                        print("%i FOUND Index: %i Hash: %s match with %s" %
#                              (len(self.valid_keys),self.counter,self.md5.hexdigest() ,n))
                        if n not in self.valid_keys:
                            self.valid_keys.append(n)
        self.candidate_keys = [x for x in self.candidate_keys if x not in delete_list]


    def run(self):
        while len(self.valid_keys) < 63:
            self.counter += 1
            self.__gen_next_key()
            self.__eval_candidate_key()
            self.__eval_valid_key()



def star1():
    onetimepad = OTP(SALT)
    onetimepad.run()
    return onetimepad.valid_keys[63][0]


if __name__ == '__main__':
    print("Star 1: ", star1())
#    print("Star 2: ", star2())

