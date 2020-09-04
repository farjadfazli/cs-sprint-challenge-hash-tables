def intersection(arrays):

    hash_table = {}
    result = []

    array1 = arrays[0]
    array2x = arrays[1:]

    for x in array1:
        hash_table[x] = 1

    for y in array2x:
        for x in y:
            if hash_table.get(x):
                hash_table[x] += 1

    for key in hash_table:
        if hash_table[key] == len(arrays):
            result.append(key)

    return result


result = intersection([
            [1,2,3],
            [1,4,5],
            [1,6,7]
        ])

print(result)


# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

#     print(intersection(arrays))
