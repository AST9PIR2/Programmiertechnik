def search_array(array, x):

# durchsucht ein array, nach dem Eingabeparamter x und gibt dessen Position im array aus

    for n in array:
        if n == x:
            return n-1
    return None


print(search_array([1,2,3,3,4,5,3 ], 3))