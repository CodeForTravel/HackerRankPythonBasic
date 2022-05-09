#!/bin/python

import math
import os
import random
import re
import sys


class Car:
    def __init__(self, max_speed, speed_unit):
        self.max_speed = max_speed
        self.speed_unit = speed_unit

    def __str__(self):
        output_text = f"Car with the maximum speed of {self.max_speed} {self.speed_unit}"
        return output_text


class Boat:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def __str__(self):
        output_text = f"Boat with the maximum speed of {self.max_speed} knots"
        return output_text


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        vehicle_type, params = args[0], args[1:]
        if vehicle_type == "car":
            max_speed, speed_unit = int(params[0]), params[1]
            vehicle = Car(max_speed, speed_unit)
        elif vehicle_type == "boat":
            max_speed = int(params[0])
            vehicle = Boat(max_speed)
        else:
            raise ValueError("invalid vehicle type")
        fptr.write("%s\n" % vehicle)
    fptr.close()
