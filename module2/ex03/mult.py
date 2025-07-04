#!/bin/bash

first_number = int(input("Enter the first number:\n"))
second_number = int(input("Enter the second number:\n"))
result = first_number * second_number

print(f"{first_number} x {second_number} = {result}")

if result < 0:
    print("The result is negative.")
elif result > 0:
    print("The result is positive.")
else:
    print("The result is positive and negative.")