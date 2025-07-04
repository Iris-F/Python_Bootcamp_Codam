#!/usr/bin/env python3
import sys
import re


if len(sys.argv) > 1:
    print("Parameters: ", len(sys.argv)-1)
    for i in range(len(sys.argv)):
        print(sys.argv[i])
else:
    print("none")