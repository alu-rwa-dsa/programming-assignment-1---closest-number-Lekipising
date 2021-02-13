# array
# sort array
# find closest numbers - smallest absolute difference
# find all pairs


def ClosestNumbers(arr):
    arr.sort()
    diff = arr[0] - arr[1]
    n = len(arr)
    start = n
    pair = []
    while True:
        d = arr[(n - start)] - arr[(n - (start - 1))]
        if abs(d) < abs(diff):
            diff = d
            pair.clear()
            pair.append(arr[(n - start)])
            pair.append(arr[(n - (start - 1))])
        elif abs(d) == abs(diff):
            pair.append(arr[(n - start)])
            pair.append(arr[(n - (start - 1))])
        
        start -= 1

        if start == 2:
            break
    
    return pair


list1 = [3, 6, 1, 7, 12, 4, 19, 2, 22, 21]   # sample

print(ClosestNumbers(list1))
