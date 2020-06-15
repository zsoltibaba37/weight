#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
from termcolor import cprint

class Weight:
    def __init__(self, l, w, t):
        self.d = 7.85   # Density
        self.l = l      # Length
        self.w = w      # Width
        self.t = t      # Thickness

    def get_dimension(self):
        return "%2.2fmm %2.2fmm %2.2fmm" % (self.l, self.w, self.t)

    def set_density(self, d):
        self.d = d

    def get_weight(self):
        s = self.l * self.w * self.t * self.d / 10 ** 6
        if s < 1:
            m = "gram"
            s = str("{:.2f}".format(s * 10 ** 3))
            return s + m
        else:
            s = str("{:.2f}".format(s))
            m = "kg"
            return s + m


class Checkint:
    def __init__(self, t):
        self.t = t
        self.i = 0

    def check(self):
        while True:
            try:
                self.i = float(input(f'The plate {self.t} (mm): '))
                if self.i <= 0:
                    self.i = 0
                else:
                    pass
                    return self.i
                z = 4 / self.i
                break
            except ValueError:
                print("This is not a number or not integer/float number!")
            except ZeroDivisionError:
                print("The value is zero or negative!")
            except KeyboardInterrupt:
                sys.exit(0)


def main():
    while True:
        print("#" * 80)
        plate = Weight(Checkint("Length").check(), Checkint("Width").check(), Checkint("Thickness").check())
        print("#" * 80)
        print("The plate size  : {}".format(plate.get_dimension()))
        cprint("The plate weight: {}".format(plate.get_weight()), 'cyan')
        plate.get_dimension()


if __name__ == '__main__':
    main()

