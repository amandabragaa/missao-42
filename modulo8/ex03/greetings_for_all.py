#!/usr/bin/env python3 
import sys


def greetings(*msg):
    if str(*msg) == "":
        print("Hello, noble stranger.")
    elif "str" in str(type(*msg)) :
        print(f"Hello, {str(*msg)}.")
    else:
        print("Error! It was not a name.")
        
    

greetings("mariana")
greetings("amanda")
greetings()
greetings(42)