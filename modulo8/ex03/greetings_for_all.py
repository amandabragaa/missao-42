#!/usr/bin/env python3 
import sys


def shrink(param1):
    print(param1[0:8])

def greetings(*msg):
    if str(*msg) == "":
        print("Hello, noble stranger.")
    elif "str" in str(type(*msg)) :
        print(f"Hello, {str(*msg)}.")
    else:
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)