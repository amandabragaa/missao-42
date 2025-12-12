#!/usr/bin/env python3 
import sys


def shrink(param1):
    print(param1[0:8])

def shrink(param1):
    print(param1[0:8])

def enlarge(param2):
    print(f"{param2}{(8-len(param2))*'Z'}")

if len(sys.argv) <= 1:
    print("none")
for item in sys.argv[1:]:
    if len(item) > 8:
        shrink(item)
    elif len(item) < 8:
        enlarge(item)
    elif len(item) == 8:
        print(item)