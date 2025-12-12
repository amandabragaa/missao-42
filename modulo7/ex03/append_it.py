#!/usr/bin/env python3 
import sys

argumento = len(sys.argv)

if argumento <= 1:
    print("none")
else:
    cont = 1
    while cont < len(sys.argv):
        if not sys.argv[cont].endswith("ism"):
            print(f"{sys.argv[cont]}ism")
        cont += 1