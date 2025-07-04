#!/usr/bin/env python3
import sys
import re

if len(sys.argv) == 3:
    search = sys.argv[2]
    keyword = sys.argv[1]
    result = re.findall(keyword, search)
    print(len(result))
else:
    print("none")