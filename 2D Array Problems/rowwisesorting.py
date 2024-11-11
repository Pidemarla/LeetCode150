def rowwisesorting(arr):
    rowlen = len(arr)
    collen = len(arr[0])
    for i in range(rowlen):
        for j in range(collen):
            swapped = False
            for k in range(collen-j-1):
                if arr[i][k] > arr[i][k+1]:
                    arr[i][k],arr[i][k+1] = arr[i][k+1], arr[i][k]
                    swapped = True
            if not swapped:
                break
    return arr

arr = [
    [5,2,1],
    [4,5,5],
    [7,5,9]
    ]
rowwisesorting = rowwisesorting(arr)
print(rowwisesorting)