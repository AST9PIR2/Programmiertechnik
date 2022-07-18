def is_odd(x):

    return bool(x % 2)


for i in range(-20, 20):
    if is_odd(i):
        print(i)
