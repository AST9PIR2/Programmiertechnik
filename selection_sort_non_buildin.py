def selection_sort_non_buildin(array, asc):

# sortiert das array, wenn asc auf True, steigend.

    list = []
    temp = array[0]

    for n in array:
        if temp < n:
            temp = n
        list.append(temp)
    if asc == False:
        list = list[::-1]

    return list

print(selection_sort_non_buildin([1,2,3,3,4,5,3,2], False))
