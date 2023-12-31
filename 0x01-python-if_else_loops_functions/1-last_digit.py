#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = number % 10 if number >= 0 else number % -10

message = f"Last digit of {number} is {last_digit} and"

if last_digit > 5:
    message += " is greater than 5"
elif last_digit == 0:
    message += " is 0"
elif last_digit < 6 and last_digit != 0:
    message += " is less than 6 and not 0"

print(message)
