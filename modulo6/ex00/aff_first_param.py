#!/usr/bin/env python3 
import sys

tam = len(sys.argv)
if tam <= 1:
    print("none")
else:
    num_arg = sys.argv[1]
    print(num_arg)