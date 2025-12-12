#!/usr/bin/env python3
cont = 0
num = int(input("Insira um numero: "))

while cont <= 9:
    result = num * cont
    print(f"{num} x {cont} = {result}")
    cont += 1