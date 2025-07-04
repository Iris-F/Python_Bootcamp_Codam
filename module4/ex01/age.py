#!/usr/bin/env python3

age = int(input("Please tell me your age: "))
future_years = 10
print(f"You are currently {str(age)} years old.")
while future_years <= 30:
    print(f"In {future_years} years, you'll be " + (str(age+future_years)) + " years old.")
    future_years += 10