#!/usr/bin/env python3 
import sys

argumento = len(sys.argv)

if argumento < 2:
    print("none")
else:
    print(f"parameters: {argumento-1}")
    for numbers in range(1, argumento):
        print(f"{sys.argv[numbers]}: {len(sys.argv[numbers])}")