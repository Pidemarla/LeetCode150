def sumofeachrow(arr):
    rowlen = len(arr)
    collen = len(arr[0])
    sumlist = []
    for i in range(rowlen):
        sum = 0
        for j in range(collen):
            sum += arr[i][j]
        sumlist.append(sum)
    return sumlist

arr = [[1,2,3],[4,5,6],[7,8,9]]
sumlist = sumofeachrow(arr)
print(sumlist)