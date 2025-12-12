#!/usr/bin/env python3
num = 0
num = int(input("Digite um numero de 1 a 25: "))

if num > 25:
    print("Erro")
else:
    while num <= 25:
        print(num)
        num += 1
        