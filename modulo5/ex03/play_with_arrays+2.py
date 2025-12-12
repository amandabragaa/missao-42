#!/usr/bin/env python3 

num = [2, 8, 9, 48, 8, 22, -12, 2]
print("Original array: ", num)

cont = 0
num_set = set([])
while cont < len(num):
    if num[cont] > 5:
        num[cont] = num[cont] + 2
        num_set.add(num[cont])
    cont += 1
    

print("New array: ", num_set)

