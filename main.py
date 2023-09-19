import random

def approximation(numberOfPoints):
    x = 0
    y = 0
    count = 0
    for i in range(numberOfPoints):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if pow(x,2) + pow(y,2) <= 1:
            count += 1
    return 4 * count / numberOfPoints

print(approximation(10))
print(approximation(100))
print(approximation(1000))
print(approximation(10000))
print(approximation(100000))
print(approximation(1000000))
print(approximation(10000000))
print(approximation(100000000))