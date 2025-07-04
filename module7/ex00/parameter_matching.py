#!/usr/bin/env python3
import sys

if len(sys.argv) == 2:
    param = sys.argv[1]
    keyword = input("What was the parameter? ")
    if keyword == param:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")