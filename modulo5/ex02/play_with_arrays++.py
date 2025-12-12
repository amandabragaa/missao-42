#!/usr/bin/env python3 

num = [2, 8, 9, 48, 8, 22, -12, 2]
print("Original array: ", num)

cont = 0
num2 = []
while cont < len(num):
    if num[cont] > 5:
        num[cont] = num[cont] + 2
        num2.append(num[cont])
    cont = cont + 1
    

print("New array: ", num2)



