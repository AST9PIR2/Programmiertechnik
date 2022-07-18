import math


def is_prime(x):

    #  prüft ob eine Zahl eine Primzahl ist

    if x < 2:
        return False
    for n in range(2, int(math.sqrt(x)+1)):
        if x % n == 0:
            return False
    return True

# print(fast_prime(9))


for i in range(-20, 20):
    if is_prime(i):
        print(i)
