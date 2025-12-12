#!/usr/bin/env python3 
import sys

tam = len(sys.argv)
if tam <= 1:
    print("none")
else:
    num_revers = sys.argv[::1]

    index = len(num_revers) - 1
    while index > 0:
        print(num_revers[index])
        index -= 1