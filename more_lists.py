from random import *
random_numbers = [randint(1, 100) for i in range(100)]

frequencies = [random_numbers.count(i) for i in range(1, 101)]

print(frequencies)
print(len(frequencies))
