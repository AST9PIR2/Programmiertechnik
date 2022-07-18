def get_digits(n):
    a = []
    for i in str(n):
        a.append(i)

    return a


def calc_faculty(n):
    sum = 1

    for i in range(1, n + 1):
        sum *= i
    return sum


def digits_factorial(n):
    result = 0
    for x in range(1, n + 1):
        sum = 0
        list = get_digits(x)
        for i in list:
            sum += calc_faculty(int(i))
        if x > 2 and sum == x:
            result += sum
    return result

print(digits_factorial(1000))