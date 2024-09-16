"""
A program that generates 10000 random numbers between 1 and 100
and it will count the numbers that are divisible by 12
"""
from random import randint
count = 0
for i in range(10000):
    random_num = randint(1,100)
    if random_num % 12 == 0:
        count += 1

    print(f"There are {count} numbers divisible by 12 between 1 and 100 in this loop")
