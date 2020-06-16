#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys, os
from termcolor import cprint


class Weight:
    """
    Calculate the weight of plate
    """

    def __init__(self, l, w, t):
        """
        :param l: Length
        :param w: Width
        :param t: Thickness
        """
        self.d = 7.85  # Density
        self.l = l  # Length
        self.w = w  # Width
        self.t = t  # Thickness

    def get_dimension(self):
        """
        :return: %2.2fmm %2.2fmm %2.2fmm
        Return the plate size
        """
        return "%2.2fmm × %2.2fmm × %2.2fmm" % (self.l, self.w, self.t)

    def set_density(self, d):
        """
        :param d: Density
        Adjusts the density of the steel
        """
        self.d = d

    def get_weight(self):
        """
        :return:  {:.2f} "gram" or {:.2f} "kg"
        The calculated weight is less than or greater than one kg
        """
        s = self.l * self.w * self.t * self.d / 10 ** 6
        if s < 1:
            m = "gram"
            s = str("{:.2f}".format(s * 10 ** 3))
            return s + m
        else:
            s = str("{:.2f}".format(s))
            m = "kg"
            return s + m


class Chk_float:
    """
    Check the input field
    Is that float number or something else
    """

    def __init__(self, t):
        """
        :param t: String
        The plate {self.t} (mm):
        Example: Chk_float("Length")
        """
        self.t = t
        self.f = 0.0

    def check(self):
        """
        :return: self.f
        It asks for one of the parameters of the plate
        Return inspected float number
        """
        while True:
            try:
                self.f = float(input(f'What is the {self.t} of plate?{" " * (9 - len(self.t))} (mm): '))
                if self.f <= 0:
                    self.f = 0.0
                else:
                    pass
                    return self.f
                z = 4 / self.f
                break
            except ValueError:
                cprint("This is not a number or not integer/float number!", 'red')
            except ZeroDivisionError:
                cprint("The value is zero or negative!", 'red')


def main():
    print("#" * 80)
    print("Welcome".center(80))
    print("This program calculate the weight of a plate".center(80))
    while True:
        print("Press Ctrl-C to Exit".center(80))
        print("#" * 80)
        plate = Weight(Chk_float("Length").check(), Chk_float("Width").check(), Chk_float("Thickness").check())
        print("#" * 80)
        cprint("The plate size is  : {}".format(plate.get_dimension()), 'cyan')
        cprint("The plate weight is: {}".format(plate.get_weight()), 'green')
        print("#" * 80)
        input("Press Enter to Continue...".center(80))
        os.system('cls' if os.name == 'nt' else 'clear')
        print("#" * 80)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nBye Bye!")
