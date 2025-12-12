#!/usr/bin/env python3 


try: 
    num = float(input("Me de um numero: "))

    if num % 1 == 0:
        print("Este número é um inteiro.")
    else:
        print("Este número é um decimal.")
    
except ValueError:
    print("Erro")