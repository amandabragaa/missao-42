#!/usr/bin/env python3 

num = [2, 8, 9, 48, 8, 22, -12, 2]
print("Original array: ", num)

cont = 0

while cont <= 7:
    num[cont] = num[cont] + 2
    cont += 1

print("New array: ", num)
