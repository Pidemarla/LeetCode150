def MaxElement(arr):
    rowlen = len(arr)
    collen = len(arr[0])
    maxnumber = 0
    for i in range(rowlen):
        for j in range(collen):
            if arr[i][j] > maxnumber:
                maxnumber = arr[i][j]
    return maxnumber

arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
MaxElement = MaxElement(arr)
print(MaxElement)