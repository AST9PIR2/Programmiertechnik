def sum_array(array):

# summiert alle interger einer liste, auch interger der unterlisten auf

    result = 0

    for n in array:
        if type(n) == int:
            result += n
        elif type(n) == list:
            result += sum_array(n)
    return result

print(sum_array(["Hello", 2, "World",[1,2], True, 3, 4.5]))