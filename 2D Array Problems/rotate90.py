#Transpose the array and reverse the row
def Transpose(arr):
    rowlen = len(arr)
    collen = len(arr[0])

    AT = [[0]*rowlen for _ in range(collen)]
    for i in range(collen):
        for j in range(rowlen):
            AT[i][j] = arr[j][i]
    return AT
def rotate90(arr):
    arr1 = Transpose(arr)
    for i in range(len(arr1)):
        arr1[i].reverse()
    return arr1
arr = [[1,2,3,],[4,5,6,],[7,8,9]]
rotate90 = rotate90(arr)
print(rotate90)   