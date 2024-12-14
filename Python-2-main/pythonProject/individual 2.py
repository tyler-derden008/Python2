#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def main():
num1 = int(input("Введи первое число (n < 100): "))
    num2 = int(input("Введи второе число (n < 100): "))
    num3 = int(input("Введи третье число (n < 100): "))
    if num1 >= 100 or num2 >= 100 or num3 >= 100:
        print("Все числа должны быть меньше 100, переделывай.")
        return
    max_num = max(num1, num2, num3)
    print(f"Наибольшее число: {max_num}")
if __name__ == "__main__":
    main()
