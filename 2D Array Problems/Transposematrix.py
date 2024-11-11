def Transpose(arr):
    rowlen = len(arr)
    collen = len(arr[0])

    AT = [[0]*rowlen for _ in range(collen)]
    for i in range(collen):
        for j in range(rowlen):
            AT[i][j] = arr[j][i]
    return AT
arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
AT = Transpose(arr)
print(AT)   