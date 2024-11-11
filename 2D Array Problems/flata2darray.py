def flat2DArray(arr):
    rowlen = len(arr)
    collen = len(arr[0])
    flatlist = []
    for i in range(rowlen):
        for j in range(collen):
            flatlist.append(arr[i][j])
    return flatlist

arr = [
    [1,2,5],
    [4,5,5],
    [7,5,9]
    ]
value = 5
flat2DArray = flat2DArray(arr)
print(flat2DArray)