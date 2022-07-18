def selection_sort(array, asc):

# sortiert das array, wenn asc auf True, steigend.

    return sorted(array, reverse=not asc)

print(selection_sort([2,4,6,5,3,1], True))