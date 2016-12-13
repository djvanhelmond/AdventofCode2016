#!/usr/local/bin/python3
from collections import OrderedDict
import copy
import time

class Facility():
    def __init__(self):
        self.Facility_items = OrderedDict()
        self.Elevator_items = []
        self.Elevator_floor = 1
        self.Elevator_steps = 0
        self.handled_this_step = []


    def Elevator_up(self):
        if (0 < len(self.Elevator_items) <= 2) and (self.Elevator_floor < 4):
            self.Elevator_steps = self.Elevator_steps + 1
            self.Elevator_floor = self.Elevator_floor + 1
            for item in self.Elevator_items:
                self.Facility_items[item] = self.Elevator_floor
            self.handled_this_step = []
            return True
        else:
            return False


    def Elevator_down(self):
        if (0 < len(self.Elevator_items) <= 2) and (self.Elevator_floor > 1):
            self.Elevator_steps = self.Elevator_steps + 1
            self.Elevator_floor = self.Elevator_floor - 1
            for item in self.Elevator_items:
                self.Facility_items[item] = self.Elevator_floor
            self.handled_this_step = []
            return True
        else:
            return False

    def Elevator_load(self, item):
        if (len(self.Elevator_items) <= 2) and (self.Facility_items[item] == self.Elevator_floor):
            self.Elevator_items.append(item)
            self.handled_this_step.append(item)
            return True
        else:
            return False

    def Elevator_unload(self, item):
        if (item in self.Elevator_items):
            self.Elevator_items.remove(item)
            self.handled_this_step.append(item)
            return True
        else:
            return False

    def add_item(self, item, floor):
        self.Facility_items[item] = floor

    def show(self):
        print("==================== - step: %i" % self.Elevator_steps)
        for n in reversed(range(1,5)):
            draw_floor = []
            draw_floor.extend(["F", str(n), " "])
            if self.Elevator_floor  == n:
                draw_floor.extend("E ")
            else:
                draw_floor.extend(". ")
            for i in self.Facility_items:
                if self.Facility_items[i] == n:
                    draw_floor.extend([i, " "])
                else:
                    draw_floor.extend(" . ")
            print(''.join(draw_floor))
        print("E: ", self.Elevator_items, "\n")

    def nothing_broken(self):
        microchips = []
        rtgs = []
        for item in self.Facility_items:
            if item[-1] == "M":
                microchips.append(item)
            else:
                rtgs.append(item)
        for microchip in microchips:
            for rtg in rtgs:
                if self.Facility_items[microchip] == self.Facility_items[rtg] \
                        and self.Facility_items[microchip] != self.Facility_items[microchip[:-1]+"G"]:
                    return False
        return True

    def can_machine_assemble(self):
        return all([ self.Facility_items[i] is 4 for i in self.Facility_items ])

    def give_options(self):
        options = []
        if self.can_machine_assemble():
            options.append(["FINISH", f.Elevator_steps])
        if len(self.Elevator_items) != 0:
            for item in self.Elevator_items:
                if (item not in self.handled_this_step):
                    options.append(["UNLOAD", item])
        for item in self.Facility_items:
            if (self.Facility_items[item] == self.Elevator_floor) \
                    and (item not in self.Elevator_items) \
                    and (item not in self.handled_this_step) \
                    and (len(self.Elevator_items) < 2):
                options.append(["LOAD", item])
        n = copy.deepcopy(self)
        if n.Elevator_up() and n.nothing_broken():
            options.append(["E_UP", None])
        n = copy.deepcopy(self)
        if n.Elevator_down() and n.nothing_broken():
            options.append(["E_DOWN", None])
        return options


    def branch(self, options, last_option):
        inverse_option = []
        if last_option[0] == "LOAD":
            inverse_option = ["UNLOAD", last_option[1]]
            print("inverse option:", inverse_option)
        if last_option[0] == "UNLOAD":
            inverse_option = ["LOAD", last_option[1]]
            print("inverse option:", inverse_option)
        if last_option[0] == "E_UP":
            inverse_option = ["E_DOWN", None]
            print("inverse option:", inverse_option)
        if last_option[0] == "E_DOWN":
            inverse_option = ["E_UP", None]
            print("inverse option:", inverse_option)

        if inverse_option in options:
            options.remove(inverse_option)


        print("=====")
        self.show()
        print("remaining:", options)
        print("last option:", last_option)
#        time.sleep(2)
        print("remaining:", options)
#        time.sleep(20)

        self.show()
        print("remaining:", options)
        print("handled: ", self.handled_this_step)
        for option in options:
            print("Branch chosen: ", option)
            if option[0] == "FINISH":
                print("Finished in %i steps" % (option[1]))
            elif option[0] == "LOAD":
                f = copy.deepcopy(self)
                f.show()
                print("LOAD BREAK", f.give_options())
                f.Elevator_load(option[1])
                f.show()
                print("LOAD BREAK", f.give_options())
                f.branch(f.give_options(), option)
            elif option[0] == "UNLOAD":
                f = copy.deepcopy(self)
                f.show()
                print("UNLOAD BREAK", f.give_options())
                f.Elevator_unload(option[1])
                f.show()
                print("UNLOAD BREAK", f.give_options())
                f.branch(f.give_options(), option)
            elif option[0] == "E_UP":
                f = copy.deepcopy(self)
                f.show()
                print("BREAK", f.give_options())
                f.Elevator_up()
                f.show()
                print("BREAK", f.give_options())
                f.branch(f.give_options(), option)
            elif option[0] == "E_DOWN":
                f = copy.deepcopy(self)
                f.show()
                print("BREAK", f.give_options())
                f.Elevator_down()
                f.show()
                print("BREAK", f.give_options())
                f.branch(f.give_options(), option)



f = Facility()
f.add_item("HG", 2)
f.add_item("HM", 1)
f.add_item("LG", 3)
f.add_item("LM", 1)
f.branch(f.give_options(), ['START', None])

"""
f.Elevator_load("HM")
f.show()
f.Elevator_up()             # step 1
f.show()
f.Elevator_load("HG")
f.show()
f.Elevator_up()             # step 2
f.show()
f.Elevator_unload("HG")
f.show()
f.Elevator_down()             # step 3
f.show()
f.Elevator_down()             # step 4
f.show()
f.Elevator_load("LM")
f.show()
f.Elevator_up()             # step 5
f.show()
f.Elevator_up()             # step 6
f.show()
f.Elevator_up()             # step 7
f.show()
f.Elevator_unload("LM")
f.show()
f.Elevator_down()             # step 8
f.show()
f.Elevator_unload("HM")
f.show()
f.Elevator_load("HG")
f.show()
f.Elevator_load("LG")
f.show()
f.Elevator_up()             # step 9
f.show()
f.Elevator_unload("HG")
f.show()
f.Elevator_unload("LG")
f.show()
f.Elevator_load("LM")
f.show()
f.Elevator_down()             # step 10
f.show()
f.Elevator_load("HM")
f.show()
f.Elevator_up()             # step 11
f.show()
"""


