def sigma(n):

    result = 0

    for x in range(1, n+1):
        if n % x == 0:
            result += x

    return result

def S(m,d):

    result = 0

    for x in range(1, m+1):
        if sigma(x) % d == 0:
            result += x
    return result

print(S(20, 7))