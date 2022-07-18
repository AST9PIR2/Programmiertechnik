def is_triangular(x):

# prüft und gibt True aus wenn sie eine Dreieckszahl ist

    for n in range(0, x + 1):
        if x == (n*(n+1))/2:
            return True
    return False


for i in range(-20, 20):
    if is_triangular(i):
        print(i)

