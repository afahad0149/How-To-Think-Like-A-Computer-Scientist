#print(list(range(10, 0, -2))) # [10, 8, 6, 4, 2]

#print(list(range(0, 10, -2)))   # [] returns empty list

#print(range(10, 0 , -2))       # prints range(10, 0, -2) Lazy promise not implemented

#relationship as code

def range_implemented(start, stop, step):
    result = []
    while (start < stop):
        result.append(start)
        start += step
    return result


