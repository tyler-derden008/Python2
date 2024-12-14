#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def pencil(n):
    if 11 <= n % 100 <= 19:
        return "карандашей"
    elif n % 10 == 1:
        return "карандаш"
    elif 2 <= n % 10 <= 4:
        return "карандаша"
    else:
        return "карандашей"
def main():
    n = int(input("Введите количество карандашей: "))
    pencil_w = pencil(n)
    print(f"Я купил {n} {pencil_w}.")
if __name__ == "__main__":
    main()

