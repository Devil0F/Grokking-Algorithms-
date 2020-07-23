def QuickSort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr.pop(0)
    left = [i for i in arr if i <= pivot]
    right = [i for i in arr if i > pivot]
    return QuickSort(left) + [pivot] + QuickSort(right)
arr = [10,5]
print(QuickSort(arr))
