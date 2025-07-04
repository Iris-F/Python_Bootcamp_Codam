#!/usr/bin/env python3

table = 0
while table < 11:
    print(f"Table of {table}:", end = " ")
    multiplier = 0
    while multiplier < 11:
        print(table*multiplier, end = " ")
        multiplier += 1
    table += 1
    print("")