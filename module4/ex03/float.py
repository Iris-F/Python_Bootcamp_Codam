#!/usr/bin/env python3

number = float(input("Give me a number: "))

if number-int(number) > 0:
    print("This number is a decimal.")
else:
    print("This number is an integer.")