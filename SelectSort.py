def selectSort(arr):
    result = []
    index = 0
    while(arr):
        for i in range(len(arr)):
            index = 0
            max = arr[0]
            if arr[i] > max:
                max = arr[i]
                index = i
        result.append(max)
        arr.pop(index)
    return result

a = [8797997,87,5,69,117]
print(selectSort(a))
