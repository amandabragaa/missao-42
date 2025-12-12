#!/usr/bin/env python3 
import math


try: 
    num = float(input("Me de um numero: "))
    num = math.ceil(num)
    print(num)
    
except ValueError:
    print("Erro")