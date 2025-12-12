#!/usr/bin/env python3
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

result = num1 * num2

if result > 0:
    print(int(num1), "*", int(num2), "=", int(result) ,"\nO resultado e positivo.")
elif result < 0:
    print(int(num1), "*", int(num2), "=", int(result) ,"\nO resultado e negativo.")
else:
    print(int(num1), "*", int(num2), "=", int(result) ,"\nO resultado e positivo e negativo.")
