def kthElement(Arr1, Arr2, k):
    # initialize array index at the start position
    a = 0
    b = 0
    x = 0

    # initialize a new array
    newArr = [0] * (len(Arr1) + len(Arr2))
    while a < len(Arr1) and b < len(Arr2):
        if Arr1[a] < Arr2[b]:
            newArr[x] = Arr1[a]
            a += 1
            x += 1
        else:
            newArr[x] = Arr2[b]
            b += 1
            x += 1
    print(newArr)

    return newArr[k-1]


array1 = [1, 2, 3, 5, 6]
array2 = [3, 4, 5, 6, 7]


print(kthElement(array1, array2, 5))
