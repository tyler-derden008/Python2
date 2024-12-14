#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

for x in range(0, 11):  # Максимум 10 быков, так как 10 * 10 = 100
    for y in range(0, 21):  # Максимум 20 коров, так как 5 * 20 = 100
        z = 100 - x - y
        if z >= 0 and (10 * x + 5 * y + 0.5 * z == 100):
            print(f"Быков: {x}, Коров: {y}, Телят: {z}")
