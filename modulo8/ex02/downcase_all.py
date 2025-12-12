#!/usr/bin/env python3 
import sys


def downcase_it():
    if len(sys.argv) == 1:
        print("none")
    else:   
        cont = 1
        while cont < len(sys.argv):
            nome = sys.argv[cont]
            print(nome.lower())
            cont = cont + 1

downcase_it()
