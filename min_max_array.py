def max_array(array, asc):

    #    return max(array), min(array)
    if array:
        temp = array[0]
    else:
        return None

    for n in array:
        if asc is False:
            if temp < n:
                temp = n
        elif asc is True:
            if temp > n:
                temp = n
    return temp

print(max_array([], False))

