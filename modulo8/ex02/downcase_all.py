#!/usr/bin/env python3 
import sys


def downcase_it(pequeno):
    print(pequeno.lower())
       
if len(sys.argv) == 1:
        print("none")
else:    
    for piquinin in sys.argv[1:]:
        downcase_it(piquinin)
