import math

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

#print(fast_prime(9))
for i in range(0,1000):
    if is_prime(i):
        print(i)